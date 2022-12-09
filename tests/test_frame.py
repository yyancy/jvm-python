from rtda.frame import *


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
