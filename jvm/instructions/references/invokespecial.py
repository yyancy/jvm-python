
from jvm.instructions.base.method_invoke_logic import invoke_method
from jvm.rtda.heap.cp_methodref import MethodRef
from jvm.rtda.heap.method_lookup import lookup_method_in_class
from ..base.instruction import *

from jvm.rtda.frame import Frame
from ...rtda.heap import constant_pool
from ...rtda.heap import cp_classref
from ...rtda.heap import object


class INVOKE_SPECIAL(Index16Instuction):
  def execute(self, frame: Frame):
    current_class = frame.method.clazz
    cp = current_class.constant_pool
    method_ref: MethodRef = cp.get_constant(self.index)
    resolved_class = method_ref.resolved_class()
    resolved_method = method_ref.resolved_method()

    if resolved_method.name == '<init>' and resolved_method.clazz != resolved_class:
      raise SystemExit('java.lang.NoSuchMethodError')
    if resolved_method.is_static():
      raise SystemExit('java.lang.IncompatibleClassChangeError')

    ref = frame.operand_stack.get_ref_from_top(
        resolved_method.arg_slot_count - 1)
    if ref == None:
      raise SystemExit('java.lang.NullPointerException')

    if (resolved_method.is_protected() and
            resolved_method.clazz.is_superclass_of(current_class) and
            resolved_method.clazz.get_package_name() != current_class.get_package_name() and
            ref.clazz != current_class and
            not ref.clazz.is_subclass_of(current_class)):
      raise SystemExit('java.lang.IllegalAccessError')

    method_to_be_invoked = resolved_method
    if (current_class.is_super() and
        resolved_class.is_superclass_of(current_class) and
            resolved_method.name == '<init>'):
      method_to_be_invoked = lookup_method_in_class(
          current_class.super_class, method_ref.name, method_ref.descriptor)
    if method_to_be_invoked == None or method_to_be_invoked.is_abstract():
      raise SystemExit('java.lang.AbstractMethodError')
    invoke_method(frame, method_to_be_invoked)
