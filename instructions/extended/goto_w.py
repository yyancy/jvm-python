from base.instruction import *

from common.cons import *
from rtda.frame import Frame


class GOTO_W(BranchInstuction):

  def fetch_operands(self, reader: BytecodeReader):
    self.offset = reader.read_u32()

  def execute(self, frame: Frame):
    super().branch(frame, self.offset)
