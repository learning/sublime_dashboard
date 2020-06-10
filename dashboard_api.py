import os
import json

import sublime

from .modules.settings import settings

api_dict = {
  'sublime/settings': settings
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
