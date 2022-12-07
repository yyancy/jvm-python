from parse import *
from classpath.new_entry import *
import classpath.classpath as classpath
import logging
from classfile.class_file import *
from objprint import op
import pprint
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
  


if __name__ == '__main__':
  cmd = parse_cmd()
  start_jvm(cmd)
