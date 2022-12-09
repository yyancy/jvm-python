import logging
import pprint

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

  print("--------test frame-----------------")
  frame = Frame(100, 100)
  test_local_vars(frame.local_vars)
  test_operand_stack(frame.operand_stack)


def test_local_vars(vars: LocalVars):
  vars.set_int(0, 100)
  vars.set_int(1, -100)
  vars.set_long(2, 2997924580)
  vars.set_long(4, -2997924580)
  vars.set_float(6, 3.1415926)
  vars.set_double(7, 2.71828182845)
  vars.set_ref(9, None)

  print(vars.get_int(0))
  print(vars.get_int(1))
  print(vars.get_long(2))
  print(vars.get_long(4))
  print(vars.get_float(6))
  print(vars.get_double(7))
  print(vars.get_ref(9))


def test_operand_stack(ops: OperandStack):
  ops.push_int(100)
  ops.push_int(-100)
  ops.push_long(2997924580)
  ops.push_long(-2997924580)
  ops.push_float(3.1415926)
  ops.push_double(2.71828182845)
  ops.push_ref(None)
  print(ops.pop_ref())
  print(ops.pop_double())
  print(ops.pop_float())
  print(ops.pop_long())
  print(ops.pop_long())
  print(ops.pop_int())
  print(ops.pop_int())


if __name__ == '__main__':
  cmd = parse_cmd()
  start_jvm(cmd)
