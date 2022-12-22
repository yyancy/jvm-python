from base.instruction import *

from common.cons import *
from rtda.frame import Frame


class IFNULL(BranchInstuction):
  def execute(self, frame: Frame):
    ref = frame.operand_stack.pop_ref()
    if ref == None:
      super().branch(frame, self.offset)


class IFNONNULL(BranchInstuction):
  def execute(self, frame: Frame):
    ref = frame.operand_stack.pop_ref()
    if ref != None:
      super().branch(frame, self.offset)
