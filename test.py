from classfile.class_file import *
import json
import pprint
from beeprint import pp
from objprint import op
# pp = pprint.PrettyPrinter(indent=4)


def print_object(o, tabdepth=0):
  for key, value in o.__dict__.items():
    print('\t'*tabdepth+key)
    if hasattr(value, '__dict__'):
      print_object(value, tabdepth+1)
    else:
      print('\t'*(tabdepth+1), value)


with open("./Demo.class", 'rb') as f:
  data = f.read()
  [cf, e] = parse(data)
  if e != None:
    raise e
  op(cf.methods)
