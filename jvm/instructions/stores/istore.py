from ..base.instruction import *
from jvm.rtda.frame import Frame


class ISTORE(Index8Instuction):
  def __init__(self) -> None:
    pass

  def fetch_operands(self, reader: BytecodeReader):
    self.val = reader.read_u8()

  def execute(self, frame: Frame):
    istore(frame, self.index)


class ISTORE_0(NoOperandsInstuction):
  def __init__(self) -> None:
    pass

  def execute(self, frame: Frame):
    istore(frame, 0)


class ISTORE_1(NoOperandsInstuction):
  def __init__(self) -> None:
    pass

  def execute(self, frame: Frame):
    istore(frame, 1)


class ISTORE_2(NoOperandsInstuction):
  def __init__(self) -> None:
    pass

  def execute(self, frame: Frame):
    istore(frame, 2)


class ISTORE_3(NoOperandsInstuction):
  def __init__(self) -> None:
    pass

  def execute(self, frame: Frame):
    istore(frame, 3)


def istore(frame: Frame, index: int):
  val = frame.operand_stack.pop_int()
  frame.local_vars.set_int(index, val)
