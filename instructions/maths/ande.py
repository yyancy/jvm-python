from ..base.instruction import *

from rtda.frame import Frame


class IAND(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    v2 = stack.pop_int()
    v1 = stack.pop_int()

    result = v1 & v2
    stack.push_int(result)


class LAND(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    v2 = stack.pop_long()
    v1 = stack.pop_long()

    result = v1 & v2
    stack.push_long(result)
