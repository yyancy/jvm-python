from ..base.instruction import *

from jvm.rtda.frame import Frame


class DADD(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    v1 = stack.pop_double()
    v2 = stack.pop_double()
    result = v1 + v2
    stack.push_double(result)


class FADD(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    v1 = stack.pop_float()
    v2 = stack.pop_float()
    result = v1 + v2
    stack.push_float(result)


class IADD(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    v1 = stack.pop_int()
    v2 = stack.pop_int()
    result = v1 + v2
    stack.push_int(result)


class LADD(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    v1 = stack.pop_long()
    v2 = stack.pop_long()
    result = v1 + v2
    stack.push_long(result)
