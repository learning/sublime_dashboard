import sublime

import os
import io
import time
import urllib
import shutil
import posixpath
import mimetypes
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn, TCPServer

from .dashboard_api import get_json_output

class DashboardServerHandler(BaseHTTPRequestHandler):

  def version_string(self):
    '''Overwrite HTTP server's version string'''
    return 'DashboardServer'

  def do_OPTIONS(self):
    '''Serve a OPTIONS request'''
    self.send_response(200, 'ok')
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    self.send_header('Access-Control-Allow-Headers', 'X-Requested-With')
    self.send_header('Access-Control-Allow-Headers', 'Content-Type')
    self.end_headers()

  def do_GET(self):
    '''Serve a GET request'''
    path = self.translate_path(self.path)

    filename = None
    f = None

    if path == '/':
      filename = self.get_static_path('index.html')
    else:
      # request static files
      filename = self.get_static_path(path.split('/', 1)[1])

    if filename and os.path.exists(filename):
      try:
        f = open(filename, 'rb')
        self.send_response(200)
        self.send_header('Content-Type', self.guess_type(filename))
        fs = os.fstat(f.fileno())
        self.send_header('Content-Length', str(fs.st_size))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Last-Modified', self.date_time_string(fs.st_mtime))
        self.end_headers()
        shutil.copyfileobj(f, self.wfile)
        f.close()
      except IOError:
        self.send_error(404, 'File not found on file system')
        return
      except:
        f.close()
        raise
    else:
      self.send_error(404, 'File not found')

  def do_POST(self):
    path = self.translate_path(self.path)
    length = int(self.headers.get('Content-Length'))
    data = self.rfile.read(length)

    if path.startswith('/api/'):
      api = path.split('/', 2)[2]
      res = get_json_output(api, data)
      f = io.BytesIO()
      f.write(res)
      f.seek(0)
      self.send_response(200)
      self.send_header('Content-Type', 'text/json')
      self.send_header('Content-Length', len(res))
      self.send_header('Access-Control-Allow-Origin', '*')
      self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
      self.send_header('Pragma', 'no-cache')
      self.send_header('Expires', '0')
      self.send_header('Last-Modified', time.time())
      self.end_headers()
      shutil.copyfileobj(f, self.wfile)
      f.close()
    else:
      self.send_error(500, 'API not available')

  def translate_path(self, path):
    # abandon query parameters
    path = path.split('?', 1)[0]
    path = path.split('#', 1)[0]
    # Don't forget explicit trailing slash when normalizing. Issue17324
    trailing_slash = path.rstrip().endswith('/')
    return posixpath.normpath(urllib.parse.unquote(path))

  def get_static_path(self, filename):
    return os.path.join(sublime.packages_path(), 'sublime_dashboard', 'dist', filename)

  def guess_type(self, path):
    base, ext = posixpath.splitext(path)
    if not mimetypes.inited:
      mimetypes.init() # try to read system mime.types
    return mimetypes.types_map.get(ext.lower(), 'application/octet-stream')

class DashboardServerThreadMixIn(ThreadingMixIn, TCPServer):
  pass

class DashboardServerThread(threading.Thread):
  httpd = None

  def __init__(self):
    # super(DashboardServerThread, self).__init__()
    super().__init__()
    self.httpd = DashboardServerThreadMixIn(('', 6618), DashboardServerHandler)
    self.setName(self.__class__.__name__)

  def run(self):
    self.httpd.serve_forever()

  def stop(self):
    self.httpd.shutdown()
    self.httpd.server_close()
