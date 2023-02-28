from ..base.instruction import *

from jvm.rtda.frame import Frame
import logging


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
  logging.info(f'local_vars {frame.local_vars.slots}')
  val = frame.local_vars.get_ref(index)
  logging.info(f'{val=} {index=}')
  frame.operand_stack.push_ref(val)
  logging.info(f'{frame.operand_stack.slots}')
