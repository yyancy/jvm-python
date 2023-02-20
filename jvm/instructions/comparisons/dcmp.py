from ..base.instruction import *

from jvm.common.cons import *
from jvm.rtda.frame import Frame


class DCMPG(NoOperandsInstuction):
  def execute(self, frame: Frame):
    dcmp(frame,True)

class DCMPL(NoOperandsInstuction):
  def execute(self, frame: Frame):
    dcmp(frame,False)




def dcmp(frame:Frame, gflag:bool):
  stack = frame.operand_stack
  v2 = stack.pop_double()
  v1 = stack.pop_double()
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
  