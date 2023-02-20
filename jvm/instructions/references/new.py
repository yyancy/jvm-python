from ..base.instruction import *

from jvm.rtda.frame import Frame
from ...rtda.heap import constant_pool
from ...rtda.heap import cp_classref
from ...rtda.heap import object


class NEW(Index16Instuction):
  def execute(self, frame: Frame):
    cp: constant_pool.ConstantPool = frame.method.clazz.constant_pool
    class_ref = cp.get_constant(self.index)

    clazz = class_ref.resolved_class()
    if clazz.is_interface() or clazz.is_abstract():
      raise SystemError("java.lang.InstantiationError")

    ref = object.Object(clazz) 
    frame.operand_stack.push_ref(ref)
    
      
