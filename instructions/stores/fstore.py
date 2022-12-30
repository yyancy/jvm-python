from base.instruction import *
from rtda.frame import Frame


class FSTORE(Index8Instuction):
  def __init__(self) -> None:
    pass

  def fetch_operands(self, reader: BytecodeReader):
    self.val = reader.read_u8()

  def execute(self, frame: Frame):
    fstore(frame, self.index)


class FSTORE_0(NoOperandsInstuction):
  def __init__(self) -> None:
    pass

  def execute(self, frame: Frame):
    fstore(frame, 0)


class FSTORE_1(NoOperandsInstuction):
  def __init__(self) -> None:
    pass

  def execute(self, frame: Frame):
    fstore(frame, 1)


class FSTORE_2(NoOperandsInstuction):
  def __init__(self) -> None:
    pass

  def execute(self, frame: Frame):
    fstore(frame, 2)


class FSTORE_3(NoOperandsInstuction):
  def __init__(self) -> None:
    pass

  def execute(self, frame: Frame):
    fstore(frame, 3)


def fstore(frame: Frame, index: int):
  val = frame.operand_stack.pop_float()
  frame.local_vars.set_float(index, val)
