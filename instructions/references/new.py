from ..base.instruction import *

from rtda.frame import Frame
from ...rtda.heap import constant_pool
from ...rtda.heap import cp_classref
from ...rtda.heap import object


class NEW(Index16Instuction):
  def execute(self, frame: Frame):
    cp: constant_pool.ConstantPool = frame.method().get_class().constant_pool
    class_ref = cp.get_constant(self.index)
    if not isinstance(class_ref, cp_classref.ClassRef):
      raise SystemExit("current reference is not a class")

    clazz = class_ref.resolved_class()
    if clazz.is_interface or clazz.is_abstract:
      raise SystemExit("java.lang.InstantiationError")

    ref = object.Object(clazz) 
    frame.operand_stack.push_ref(ref)
    
      
