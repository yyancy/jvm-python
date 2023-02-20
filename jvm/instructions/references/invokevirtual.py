
from ..base.instruction import *

from jvm.rtda.frame import Frame
from ...rtda.heap import constant_pool
from ...rtda.heap import cp_classref
from ...rtda.heap import cp_methodref
from ...rtda.heap import object
import logging
# invoke instance method; dispath based on class


class INVOKE_VIRTUAL(Index16Instuction):
  def execute(self, frame: Frame):
    cp = frame.method.clazz.constant_pool
    method_ref: cp_methodref.MethodRef = cp.get_constant(self.index)
    if method_ref.name == 'println':
      stack = frame.operand_stack
      match method_ref.descriptor:
        case "(Z)V":
          logging.info(f"{stack.pop_int()!=0}")
        case "(C)V":
          logging.info(f"{stack.pop_int()}")
        case "(B)V":
          logging.info(f"{stack.pop_int()}")
        case "(S)V":
          logging.info(f"{stack.pop_int()}")
        case "(I)V":
          logging.info(f"{stack.pop_int()}")
        case "(J)V":
          logging.info(f"{stack.pop_long()}")
        case "(F)V":
          logging.info(f"{stack.pop_float()}")
        case "(D)V":
          logging.info(f"{stack.pop_double()}")
      stack.pop_ref()
