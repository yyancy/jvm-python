from ..base.instruction import *

from jvm.rtda.frame import Frame


class ILOAD(Index8Instuction):
  def execute(self, frame: Frame):
    iload(frame, self.index)


class ILOAD_0(NoOperandsInstuction):

  def execute(self, frame: Frame):
    iload(frame, 0)


class ILOAD_1(NoOperandsInstuction):

  def execute(self, frame: Frame):
    iload(frame, 1)


class ILOAD_2(NoOperandsInstuction):

  def execute(self, frame: Frame):
    iload(frame, 2)


class ILOAD_3(NoOperandsInstuction):

  def execute(self, frame: Frame):
    iload(frame, 3)


def iload(frame: Frame, index: int):
  val = frame.local_vars.get_int(index)
  frame.operand_stack.push_int(val)
