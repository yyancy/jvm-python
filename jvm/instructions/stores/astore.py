from ..base.instruction import *
from jvm.rtda.frame import Frame
import logging

class ASTORE(Index8Instuction):

  def execute(self, frame: Frame):
    astore(frame, self.index)


class ASTORE_0(NoOperandsInstuction):
  def __init__(self) -> None:
    pass

  def execute(self, frame: Frame):
    astore(frame, 0)


class ASTORE_1(NoOperandsInstuction):
  def __init__(self) -> None:
    pass

  def execute(self, frame: Frame):
    astore(frame, 1)


class ASTORE_2(NoOperandsInstuction):
  def __init__(self) -> None:
    pass

  def execute(self, frame: Frame):
    astore(frame, 2)


class ASTORE_3(NoOperandsInstuction):
  def __init__(self) -> None:
    pass

  def execute(self, frame: Frame):
    astore(frame, 3)


def astore(frame: Frame, index: int):
  val = frame.operand_stack.pop_ref()
  logging.debug(f'astore {val=} {index=}')
  frame.local_vars.set_ref(index, val)
