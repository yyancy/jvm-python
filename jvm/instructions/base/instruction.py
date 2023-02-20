from jvm.rtda.frame import Frame
from abc import ABC, abstractmethod
from .byte_reader import BytecodeReader


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
    self.offset = reader.read_s16()


  def branch(self, frame: Frame, offset: int):
      pc = frame.thread.pc
      next_pc = pc + offset
      frame.set_next_pc(next_pc)


class Index8Instuction(Instruction):
  def __init__(self) -> None:
    super().__init__()
    self.index: int

  def fetch_operands(self, reader: BytecodeReader):
    self.index = reader.read_u8()

  def execute(self, frame: Frame):
    pass


class Index16Instuction(Instruction):
  def __init__(self) -> None:
    super().__init__()
    self.index: int

  def fetch_operands(self, reader: BytecodeReader):
    self.index = reader.read_u16()

  def execute(self, frame: Frame):
    pass
