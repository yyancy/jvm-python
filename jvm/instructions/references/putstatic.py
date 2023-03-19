import logging
from jvm.instructions.base import class_init_logic
from ..base.instruction import *

from jvm.rtda.frame import Frame
from ...rtda.heap import constant_pool
from ...rtda.heap import cp_classref
from ...rtda.heap import object
from ...rtda.heap.cp_fieldref import FieldRef


class PUT_STATIC(Index16Instuction):
  def execute(self, frame: Frame):
    current_method = frame.method
    current_class = current_method.clazz
    cp = current_class.constant_pool
    field_ref: FieldRef = cp.get_constant(self.index)
    field = field_ref.resolved_field()
    clazz = field.clazz
    if not clazz.init_started:
      frame.revert_next_pc()
      class_init_logic.init_class(frame.thread, clazz)
      return

    if not field.is_static():
      raise SystemExit('java.lang.IncompatibleClassChangeError')
    if field.is_final():
      logging.debug(f'current_class {current_class}')
      if current_class != clazz or current_method.name != '<clinit>':
        raise SystemExit('java.lang.IllegalAccessError')

    descriptor = field.descriptor
    slot_id = field.slot_id
    slots = clazz.static_vars
    stack = frame.operand_stack
    match(descriptor[0]):
      case 'Z'| 'B'|'C'| 'S'| 'I':
        slots.set_int(slot_id, stack.pop_int())
      case 'F':
        slots.set_float(slot_id, stack.pop_float())
      case 'J':
        slots.set_long(slot_id, stack.pop_long())
      case 'D':
        slots.set_double(slot_id, stack.pop_double())
      case 'L'| '[':
        slots.set_ref(slot_id, stack.pop_ref())
