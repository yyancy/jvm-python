from base.instruction import *
from rtda.frame import Frame


class LSTORE(Index8Instuction):
  def __init__(self) -> None:
    pass

  def fetch_operands(self, reader: BytecodeReader):
    self.val = reader.read_u8()

  def execute(self, frame: Frame):
    lstore(frame, self.index)


class LSTORE_0(NoOperandsInstuction):
  def __init__(self) -> None:
    pass

  def execute(self, frame: Frame):
    lstore(frame, 0)


class LSTORE_1(NoOperandsInstuction):
  def __init__(self) -> None:
    pass

  def execute(self, frame: Frame):
    lstore(frame, 1)


class LSTORE_2(NoOperandsInstuction):
  def __init__(self) -> None:
    pass

  def execute(self, frame: Frame):
    lstore(frame, 2)


class LSTORE_3(NoOperandsInstuction):
  def __init__(self) -> None:
    pass

  def execute(self, frame: Frame):
    lstore(frame, 3)


def lstore(frame: Frame, index: int):
  val = frame.operand_stack.pop_long()
  frame.local_vars.set_long(index, val)
