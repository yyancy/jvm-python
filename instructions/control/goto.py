from ..base.instruction import *

from common.cons import *
from rtda.frame import Frame


class GOTO(BranchInstuction):
  def execute(self, frame: Frame):
    super().branch(frame, self.offset)
