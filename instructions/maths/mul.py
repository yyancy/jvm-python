from base.instruction import *

from rtda.frame import Frame


class DMUL(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    v2 = stack.pop_double()
    v1 = stack.pop_double()
    result = v1 * v2
    stack.push_double(result)


class FMUL(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    v2 = stack.pop_float()
    v1 = stack.pop_float()
    result = v1 * v2
    stack.push_float(result)


class IMUL(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    v2 = stack.pop_int()
    v1 = stack.pop_int()
    result = v1 * v2
    stack.push_int(result)


class LMUL(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    v2 = stack.pop_long()
    v1 = stack.pop_long()
    result = v1 * v2
    stack.push_long(result)
