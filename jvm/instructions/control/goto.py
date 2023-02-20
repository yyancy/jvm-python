from ..base.instruction import *

from jvm.common.cons import *
from jvm.rtda.frame import Frame


class GOTO(BranchInstuction):
  def execute(self, frame: Frame):
    super().branch(frame, self.offset)
