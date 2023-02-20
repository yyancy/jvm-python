from ..base.instruction import *

from jvm.rtda.frame import Frame
from ...rtda.heap import constant_pool
from ...rtda.heap import cp_classref
from ...rtda.heap import object
from ...rtda.heap.cp_classref import ClassRef

class INSTANCE_OF(Index16Instuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    ref = stack.pop_ref()
    if ref == None:
      stack.push_int(0)
      return
    
    cp = frame.method.clazz.constant_pool
    class_ref: ClassRef = cp.get_constant(self.index)
    clazz = class_ref.resolved_class()
    if ref.is_instance_of(clazz):
      stack.push_int(1)
    else:
      stack.push_int(0)