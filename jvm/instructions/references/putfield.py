from ..base.instruction import *

from jvm.rtda.frame import Frame
from ...rtda.heap import constant_pool
from ...rtda.heap import cp_classref
from ...rtda.heap import object
from ...rtda.heap.cp_fieldref import FieldRef
import logging


class PUT_FIELD(Index16Instuction):
  def execute(self, frame: Frame):
    current_method = frame.method
    current_class = current_method.clazz
    cp = current_class.constant_pool
    field_ref: FieldRef = cp.get_constant(self.index)
    field = field_ref.resolved_field()
    clazz = field.clazz

    if field.is_static():
      raise SystemExit('java.lang.IncompatibleClassChangeError')
    if field.is_final():
      if current_class != field.clazz or current_method.name != '<init>':
        raise SystemExit('java.lang.IllegalAccessError')

    descriptor = field.descriptor
    slot_id = field.slot_id
    slots = clazz.static_vars
    stack = frame.operand_stack
    match(descriptor[0]):
      case 'Z'| 'B'| 'C'| 'S'| 'I':
        val = stack.pop_int()
        ref = stack.pop_ref()
        if ref == None:
          raise SystemExit('java.lang.NullPointerException')
        ref.fields.set_int(slot_id, val)

      case 'F':
        val = stack.pop_float()
        ref = stack.pop_ref()
        if ref == None:
          raise SystemExit('java.lang.NullPointerException')
        ref.fields().set_float(slot_id, val)
      case 'J':
        val = stack.pop_long()
        ref = stack.pop_ref()
        if ref == None:
          raise SystemExit('java.lang.NullPointerException')
        ref.fields().set_long(slot_id, val)
      case 'D':
        val = stack.pop_double()
        ref = stack.pop_ref()
        if ref == None:
          raise SystemExit('java.lang.NullPointerException')
        ref.fields().set_double(slot_id, val)
      case 'L'| '[':
        val = stack.pop_ref()
        ref = stack.pop_ref()
        if ref == None:
          raise SystemExit('java.lang.NullPointerException')
        ref.fields().set_ref(slot_id, val)
