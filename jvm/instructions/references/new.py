from ..base.instruction import *

from jvm.rtda.frame import Frame
from ...rtda.heap import constant_pool
from ...rtda.heap import cp_classref
from ...rtda.heap import object
from jvm.instructions.base import class_init_logic


class NEW(Index16Instuction):
  def execute(self, frame: Frame):
    cp: constant_pool.ConstantPool = frame.method.clazz.constant_pool
    class_ref = cp.get_constant(self.index)

    clazz = class_ref.resolved_class()
    if not clazz.init_started:
      frame.revert_next_pc()
      class_init_logic.init_class(frame.thread, clazz)
      return
      
    if clazz.is_interface() or clazz.is_abstract():
      raise SystemError("java.lang.InstantiationError")

    ref = object.Object(clazz) 
    frame.operand_stack.push_ref(ref)
    
      
