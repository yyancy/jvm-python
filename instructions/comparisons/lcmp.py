
from base.instruction import *

from common.cons import *
from rtda.frame import Frame


class LCMP(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    v2 = stack.pop_long()
    v1 = stack.pop_long()
    if v1 > v2:
      stack.push_int(1)
    elif v1 == v2:
      stack.push_int(0)
    else:
      stack.push_int(-1)


class FCMPG(NoOperandsInstuction):
  def execute(self, frame: Frame):
    fcmp(frame, True)


class FCMPL(NoOperandsInstuction):
  def execute(self, frame: Frame):
    fcmp(frame, False)


def fcmp(frame: Frame, gFlag: bool):
  stack = frame.operand_stack
  v2 = stack.pop_float()
  v1 = stack.pop_float()
  if v1 > v2:
    stack.push_int(1)
  elif v1 == v2:
    stack.push_int(0)
  elif v1 < v2:
    stack.push_int(-1)
  elif gFlag:
    stack.push_int(1)
  else:
    stack.push_int(-1)
