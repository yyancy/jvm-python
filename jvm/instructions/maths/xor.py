from ..base.instruction import *

from jvm.rtda.frame import Frame


class IXOR(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    v2 = stack.pop_int()
    v1 = stack.pop_int()
    result = v1 ^ v2
    stack.push_int(result)


class LXOR(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    v2 = stack.pop_long()
    v1 = stack.pop_long()
    result = v1 ^ v2
    stack.push_long(result)
