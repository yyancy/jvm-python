from classfile.class_file import *
from objprint import op


if __name__ == '__main__':
  with open("data/Demo.class", 'rb') as f:
    data = f.read()
    [cf, e] = parse(data)
    if e != None:
      raise e
    op(cf.methods)
