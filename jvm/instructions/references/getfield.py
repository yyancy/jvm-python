
from ..base.instruction import *

from jvm.rtda.frame import Frame
from ...rtda.heap import constant_pool
from ...rtda.heap import cp_classref
from ...rtda.heap import object
from ...rtda.heap.cp_fieldref import FieldRef
import logging

class GET_FIELD(Index16Instuction):
  def execute(self, frame: Frame):
    # current_method = frame.method
    # current_class = current_method.clazz
    cp = frame.method.clazz.constant_pool
    field_ref: FieldRef = cp.get_constant(self.index)
    field = field_ref.resolved_field()

    if field.is_static():
      raise SystemExit('java.lang.IncompatibleClassChangeError')

    stack = frame.operand_stack
    ref = stack.pop_ref()
    if ref == None:
      raise SystemExit('java.lang.NullPointerException')
    
    descriptor = field.descriptor
    slot_id = field.slot_id
    slots = ref.fields()

    match(descriptor[0]):
      case 'Z'| 'B'| 'C'| 'S'| 'I':
        stack.push_int(slots.get_int(slot_id))
      case 'F':
        stack.push_float(slots.get_float(slot_id))
      case 'J':
        stack.push_long(slots.get_long(slot_id))
      case 'D':
        stack.push_double(slots.get_double(slot_id))
      case 'L'| '[':
        stack.push_ref(slots.get_ref(slot_id))
