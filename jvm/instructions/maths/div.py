from ..base.instruction import *

from jvm.rtda.frame import Frame


class DDIV(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    v2 = stack.pop_double()
    v1 = stack.pop_double()
    result = v1 / v2
    stack.push_double(result)


class FDIV(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    v2 = stack.pop_float()
    v1 = stack.pop_float()
    result = v1 / v2
    stack.push_float(result)


class IDIV(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    v2 = stack.pop_int()
    v1 = stack.pop_int()
    assert v2 !=0, f"java.lang.ArithmeticException: / by zero"
    result = v1 // v2
    stack.push_int(result)


class LDIV(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    v2 = stack.pop_long()
    v1 = stack.pop_long()
    assert v2 !=0, f"java.lang.ArithmeticException: / by zero"
    result = v1 // v2
    stack.push_long(result)
