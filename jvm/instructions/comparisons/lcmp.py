
import logging
from ..base.instruction import *

from jvm.common.cons import *
from jvm.rtda.frame import Frame


class LCMP(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    v2 = stack.pop_long()
    v1 = stack.pop_long()
    # logging.info(f'{v1=} {v2=}')
    if v1 > v2:
      stack.push_int(1)
    elif v1 == v2:
      stack.push_int(0)
    else:
      stack.push_int(-1)
