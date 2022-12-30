from base.instruction import *
from rtda.frame import Frame


class ASTORE(Index8Instuction):
  def __init__(self) -> None:
    pass

  def fetch_operands(self, reader: BytecodeReader):
    self.val = reader.read_u8()

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
  frame.local_vars.set_ref(index, val)
