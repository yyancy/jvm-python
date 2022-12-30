from base.instruction import *

from rtda.frame import Frame


class DLOAD(Index8Instuction):
  def execute(self, frame: Frame):
    dload(frame, self.index)


class DLOAD_0(NoOperandsInstuction):

  def execute(self, frame: Frame):
    dload(frame, 0)


class DLOAD_1(NoOperandsInstuction):

  def execute(self, frame: Frame):
    dload(frame, 1)


class DLOAD_2(NoOperandsInstuction):

  def execute(self, frame: Frame):
    dload(frame, 2)


class DLOAD_3(NoOperandsInstuction):

  def execute(self, frame: Frame):
    dload(frame, 3)


def dload(frame: Frame, index: int):
  vdl = frame.locdl_vars.get_double(index)
  frame.operand_stack.push_double(vdl)
