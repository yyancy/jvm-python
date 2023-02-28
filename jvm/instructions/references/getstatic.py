
from jvm.instructions.base import class_init_logic
from ..base.instruction import *

from jvm.rtda.frame import Frame
from ...rtda.heap import constant_pool
from ...rtda.heap import cp_classref
from ...rtda.heap import object
from ...rtda.heap.cp_fieldref import FieldRef
import logging

class GET_STATIC(Index16Instuction):
  def execute(self, frame: Frame):
    current_method = frame.method
    current_class = current_method.clazz
    cp = current_class.constant_pool
    field_ref: FieldRef = cp.get_constant(self.index)
    logging.debug(f'{field_ref.name}')
    field = field_ref.resolved_field()
    clazz = field.clazz
    if not clazz.init_started:
      frame.revert_next_pc()
      class_init_logic.init_class(frame.thread, clazz)
      return

    if not field.is_static():
      raise SystemExit('java.lang.IncompatibleClassChangeError')

    descriptor = field.descriptor
    slot_id = field.slot_id
    slots = clazz.static_vars
    stack = frame.operand_stack
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
