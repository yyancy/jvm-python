from ..base.instruction import *
from rtda.frame import Frame
from common.cons import *


class IINC(Instruction):
  def __init__(self) -> None:
    self.index: uint32
    self.const: int32

  def fetch_operands(self, reader: BytecodeReader):
    self.index = uint32(reader.read_u8())
    self.const = int32(reader.read_u8())

  def execute(self, frame: Frame):
    local_vars = frame.local_vars
    val = local_vars.get_int(self.index)
    val += self.const
    local_vars.set_int(self.index, val)
