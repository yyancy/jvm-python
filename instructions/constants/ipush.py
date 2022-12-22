from base.instruction import *
from rtda.frame import Frame


class BIPUSH(Instruction):
  def __init__(self) -> None:
    self.val: int

  def fetch_operands(self, reader: BytecodeReader):
    self.val = reader.read_u8()

  def execute(self, frame: Frame):
    frame.operand_stack.push_int(self.val)


class SIPUSH(Instruction):
  def __init__(self) -> None:
    self.val: int

  def fetch_operands(self, reader: BytecodeReader):
    self.val = reader.read_u16()

  def execute(self, frame: Frame):
    frame.operand_stack.push_int(self.val)
