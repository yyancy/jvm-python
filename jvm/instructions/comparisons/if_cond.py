from ..base.instruction import *
from jvm.common.cons import *
from jvm.rtda.frame import Frame


class IFEQ(BranchInstuction):
  def execute(self, frame: Frame):
    val = frame.operand_stack.pop_int()
    if val == 0:
      self.branch(frame, self.offset)


class IFNE(BranchInstuction):
  def execute(self, frame: Frame):
    val = frame.operand_stack.pop_int()
    if val != 0:
      self.branch(frame, self.offset)


class IFLT(BranchInstuction):
  def execute(self, frame: Frame):
    val = frame.operand_stack.pop_int()
    if val < 0:
      self.branch(frame, self.offset)


class IFLE(BranchInstuction):
  def execute(self, frame: Frame):
    val = frame.operand_stack.pop_int()
    if val <= 0:
      self.branch(frame, self.offset)


class IFGT(BranchInstuction):
  def execute(self, frame: Frame):
    val = frame.operand_stack.pop_int()
    if val > 0:
      self.branch(frame, self.offset)


class IFGE(BranchInstuction):
  def execute(self, frame: Frame):
    val = frame.operand_stack.pop_int()
    if val >= 0:
      self.branch(frame, self.offset)
