import os
import json

import sublime

def get_settings(data):
  filename = os.path.join(sublime.packages_path(), 'User', 'Preferences.sublime-settings')
  try:
    f = open(filename, 'r')
    fs = os.fstat(f.fileno())
    result = {
      'error': 0,
      'data': json.loads(f.read(fs.st_size))
    }
    f.close()
    return result
  except Exception as e:
    return {
      'error': 1,
      'message': str(e)
    }

api_dict = {
  'sublime/settings': get_settings
}

def get_json_output(api, data = None):
  api_func = api_dict.get(api)
  if api_func:
    result = api_func(data)
  else:
    result = {
      'error': 1,
      'message': 'API `%` is not available' % api
    }
  return json.dumps(result).encode('utf-8')
