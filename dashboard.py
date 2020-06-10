import sublime
import sublime_plugin

import webbrowser

from .dashboard_webserver import DashboardServerThread

thread = None

class DashboardOpenCommand(sublime_plugin.ApplicationCommand):
  def run(self):
    global thread
    if thread is None:
      thread = DashboardServerThread()
      thread.start()
    webbrowser.open('http://localhost:6618')
