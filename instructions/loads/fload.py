
from base.instruction import *

from rtda.frame import Frame


class FLOAD(Index8Instuction):
  def execute(self, frame: Frame):
    fload(frame, self.index)


class FLOAD_0(NoOperandsInstuction):

  def execute(self, frame: Frame):
    fload(frame, 0)


class FLOAD_1(NoOperandsInstuction):

  def execute(self, frame: Frame):
    fload(frame, 1)


class FLOAD_2(NoOperandsInstuction):

  def execute(self, frame: Frame):
    fload(frame, 2)


class FLOAD_3(NoOperandsInstuction):

  def execute(self, frame: Frame):
    fload(frame, 3)


def fload(frame: Frame, index: int):
  val = frame.local_vars.get_float(index)
  frame.operand_stack.push_float(val)
