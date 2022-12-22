
from base.instruction import *

from common.cons import *
from rtda.frame import Frame


class TABLE_SWITCH(BranchInstuction):
  def fetch_operands(self, reader: BytecodeReader):
    reader.skip_padding()
    self.default_offset = reader.read_u32()
    self.low = reader.read_u32()
    self.high = reader.read_u32()
    jump_offsets_count = self.high - self.low + 1
    self.jump_offsets = reader.read_u32s(jump_offsets_count)

  def execute(self, frame: Frame):
    index = frame.operand_stack.pop_int()
    if index >= self.low and index <= self.high:
      offset = int(self.jump_offsets[index - self.low])
    else:
      offset = int(self.default_offset)

    super().branch(frame, offset)
