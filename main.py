import logging
import pprint
import interperter

from objprint import op

import classpath.classpath as classpath
from classfile.class_file import *
from classpath.new_entry import *
from parse import *

from rtda.frame import *

pp = pprint.PrettyPrinter(indent=4)
logging.basicConfig(format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d:%H:%M:%S',
                    level=logging.DEBUG)


def start_jvm(cmd: Cmd):
  cp = classpath.parse(cmd.XjreOption, cmd.cpOption)
  print(f"classpath:{cp} class:{cmd.clazz} args:{cmd.args}")

  class_name = cmd.clazz.replace('.', '/', -1)
  class_data, _, err = cp.read_class(class_name)
  if err != None:
    print(f"Could not find or load main class {cmd.clazz}: {err}")
    return
  print(f"class data: {class_data}")
  [cf, e] = parse(class_data)
  if e != None:
    raise e

  op(cf)

  main_method = get_main_method(cf)
  if main_method != None:
    interperter.interpret(main_method)
  else:
    logging.warning(f"Main method not found in class {cmd.clazz}")

def get_main_method(cf :ClassFile)-> MemberInfo:
  for method in cf.methods:
    if method.name() == "main" and method.descriptor() == "([Ljava/lang/String;)V":
      return method
  return None
if __name__ == '__main__':
  cmd = parse_cmd()
  start_jvm(cmd)
