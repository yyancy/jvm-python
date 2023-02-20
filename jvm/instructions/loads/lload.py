from ..base.instruction import *

from jvm.rtda.frame import Frame


class LLOAD(Index8Instuction):
  def execute(self, frame: Frame):
    lload(frame, self.index)


class LLOAD_0(NoOperandsInstuction):

  def execute(self, frame: Frame):
    lload(frame, 0)


class LLOAD_1(NoOperandsInstuction):

  def execute(self, frame: Frame):
    lload(frame, 1)


class LLOAD_2(NoOperandsInstuction):

  def execute(self, frame: Frame):
    lload(frame, 2)


class LLOAD_3(NoOperandsInstuction):

  def execute(self, frame: Frame):
    lload(frame, 3)


def lload(frame: Frame, index: int):
  val = frame.local_vars.get_long(index)
  frame.operand_stack.push_long(val)
