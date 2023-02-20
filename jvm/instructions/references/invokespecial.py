
from ..base.instruction import *

from jvm.rtda.frame import Frame
from ...rtda.heap import constant_pool
from ...rtda.heap import cp_classref
from ...rtda.heap import object

class INVOKE_SPECIAL(Index16Instuction):
  def execute(self, frame: Frame):
    # TODO: need to be implemented
    frame.operand_stack.pop_ref()