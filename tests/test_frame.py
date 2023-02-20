from jvm.rtda.frame import *

def test_frame():
  frame = Frame(100,100)
  check_local_vars(frame.local_vars)
  check_operand_stack(frame.operand_stack)

def check_local_vars(vars: LocalVars):
  vars.set_int(0, 100)
  vars.set_int(1, -100)
  vars.set_long(2, 2997924580)
  vars.set_long(4, -2997924580)
  vars.set_float(6, 3.1415926)
  vars.set_double(7, 2.71828182845)
  vars.set_ref(9, None)

  assert vars.get_int(0) == 100
  assert vars.get_int(1) == -100
  assert vars.get_long(2) ==  2997924580
  assert vars.get_long(4) ==  -2997924580
  assert vars.get_float(6) == 3.1415926
  assert vars.get_double(7) == 2.71828182845
  assert vars.get_ref(9) == None


def check_operand_stack(ops: OperandStack):
  ops.push_int(100)
  ops.push_int(-100)
  ops.push_long(2997924580)
  ops.push_long(-2997924580)
  ops.push_float(3.1415926)
  ops.push_double(2.71828182845)
  ops.push_ref(None)

  assert ops.pop_ref() == None
  assert ops.pop_double() == 2.71828182845
  assert ops.pop_float() == 3.1415926
  assert ops.pop_long() == -2997924580
  assert ops.pop_long() == 2997924580
  assert ops.pop_int() == -100
  assert ops.pop_int() == 100
