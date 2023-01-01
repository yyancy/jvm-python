from ..base.instruction import *

from rtda.frame import Frame


class ALOAD(Index8Instuction):
  def execute(self, frame: Frame):
    aload(frame, self.index)


class ALOAD_0(NoOperandsInstuction):

  def execute(self, frame: Frame):
    aload(frame, 0)


class ALOAD_1(NoOperandsInstuction):

  def execute(self, frame: Frame):
    aload(frame, 1)


class ALOAD_2(NoOperandsInstuction):

  def execute(self, frame: Frame):
    aload(frame, 2)


class ALOAD_3(NoOperandsInstuction):

  def execute(self, frame: Frame):
    aload(frame, 3)


def aload(frame: Frame, index: int):
  val = frame.local_vars.get_ref(index)
  frame.operand_stack.push_ref(val)
