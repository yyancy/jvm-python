from ..base.instruction import *

from jvm.common.cons import *
from jvm.rtda.frame import Frame


class LOOKUP_SWITCH(BranchInstuction):
  def fetch_operands(self, reader: BytecodeReader):
    reader.skip_padding()
    self.default_offset = reader.read_u32()
    self.npairs = reader.read_u32()
    self.match_offsets = reader.read_u32s(self.npairs * 2)

  def execute(self, frame: Frame):
    key = frame.operand_stack.pop_int()
    for i in range(self.npairs*2, 2):
      if self.match_offsets[i] == key:
        super().branch(frame, int(self.match_offsets[i+1]))
        return

    super().branch(frame, int(self.default_offset))