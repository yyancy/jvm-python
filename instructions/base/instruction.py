from rtda.frame import Frame
from abc import ABC, abstractmethod


class BytecodeReader:
  pass


class Instruction(ABC):
  @abstractmethod
  def fetch_operands(self, reader: BytecodeReader):
    assert False, "To be implemented"

  @abstractmethod
  def execute(self, frame: Frame):
    assert False, "To be implemented"


class NoOperandsInstuction(Instruction):

  def fetch_operands(self, reader: BytecodeReader):
    pass

  def execute(self, frame: Frame):
    pass


class BranchInstuction(Instruction):
  def __init__(self) -> None:
    super().__init__()
    self.offset: int

  def fetch_operands(self, reader: BytecodeReader):
    self.offset = reader.read_uint16()

  def execute(self, frame: Frame):
    pass

class Index8Instuction(Instruction):
  def __init__(self) -> None:
    super().__init__()
    self.index: int

  def fetch_operands(self, reader: BytecodeReader):
    self.index = reader.read_uint8()

  def execute(self, frame: Frame):
    pass
