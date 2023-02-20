
from ..base.instruction import *

from jvm.common.cons import *
from jvm.rtda.frame import Frame


class FCMPG(NoOperandsInstuction):
  def execute(self, frame: Frame):
    fcmp(frame,True)

class FCMPL(NoOperandsInstuction):
  def execute(self, frame: Frame):
    fcmp(frame,False)




def fcmp(frame:Frame, gflag:bool):
  stack = frame.operand_stack
  v2 = stack.pop_float()
  v1 = stack.pop_float()
  if v1 > v2:
    stack.push_int(1)
  elif v1 == v2:
    stack.push_int(0)
  elif v1 < v2:
    stack.push_int(-1)
  elif gflag:
    stack.push_int(1)
  else:
    stack.push_int(-1)
  