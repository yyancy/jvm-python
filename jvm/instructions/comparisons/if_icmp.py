from ..base.instruction import *
from jvm.common.cons import *
from jvm.rtda.frame import Frame


class IF_ICMPEQ(BranchInstuction):
  def execute(self, frame: Frame):
    v1, v2 = pop(frame)
    if v1 == v2:
      self.branch(frame, self.offset)


class IF_ICMPNE(BranchInstuction):
  def execute(self, frame: Frame):
    v1, v2 = pop(frame)
    if v1 != v2:
      self.branch(frame, self.offset)


class IF_ICMPLT(BranchInstuction):
  def execute(self, frame: Frame):
    v1, v2 = pop(frame)
    if v1 < v2:
      self.branch(frame, self.offset)


class IF_ICMPLE(BranchInstuction):
  def execute(self, frame: Frame):
    v1, v2 = pop(frame)
    if v1 <= v2:
      self.branch(frame, self.offset)


class IF_ICMPGT(BranchInstuction):
  def execute(self, frame: Frame):
    v1, v2 = pop(frame)
    if v1 > v2:
      self.branch(frame, self.offset)


class IF_ICMPGE(BranchInstuction):
  def execute(self, frame: Frame):
    v1, v2 = pop(frame)
    # print(f"v1 = {v1} v2 = {v2} offset={self.offset}")
    if v1 >= v2:
      self.branch(frame, self.offset)


def pop(frame: Frame) -> tuple[int, int]:
  stack = frame.operand_stack
  v2 = stack.pop_int()
  v1 = stack.pop_int()
  return [v1, v2]
