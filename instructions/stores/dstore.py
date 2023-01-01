from ..base.instruction import *
from rtda.frame import Frame


class DSTORE(Index8Instuction):
  def __init__(self) -> None:
    pass

  def fetch_operands(self, reader: BytecodeReader):
    self.val = reader.read_u8()

  def execute(self, frame: Frame):
    dstore(frame, self.index)


class DSTORE_0(NoOperandsInstuction):
  def __init__(self) -> None:
    pass

  def execute(self, frame: Frame):
    dstore(frame, 0)


class DSTORE_1(NoOperandsInstuction):
  def __init__(self) -> None:
    pass

  def execute(self, frame: Frame):
    dstore(frame, 1)


class DSTORE_2(NoOperandsInstuction):
  def __init__(self) -> None:
    pass

  def execute(self, frame: Frame):
    dstore(frame, 2)


class DSTORE_3(NoOperandsInstuction):
  def __init__(self) -> None:
    pass

  def execute(self, frame: Frame):
    dstore(frame, 3)


def dstore(frame: Frame, index: int):
  val = frame.operand_stack.pop_double()
  frame.local_vars.set_double(index, val)
