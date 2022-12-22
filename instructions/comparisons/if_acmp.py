from base.instruction import *

from common.cons import *
from rtda.frame import Frame


class IF_ACMPEQ(BranchInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    v2 = stack.pop_ref()
    v1 = stack.pop_ref()
    if v1 == v2:
      super().branch(frame, self.offset)


class IF_ACMPNE(BranchInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    v2 = stack.pop_ref()
    v1 = stack.pop_ref()
    if v1 != v2:
      super().branch(frame, self.offset)
