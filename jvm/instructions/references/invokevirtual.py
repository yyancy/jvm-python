
from jvm.instructions.base.method_invoke_logic import invoke_method
from jvm.rtda.heap.method_lookup import lookup_method_in_class
from jvm.rtda.heap.string_pool import pystring
from jvm.rtda.operand_stack import OperandStack
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
    current_class = frame.method.clazz
    cp = current_class.constant_pool
    method_ref: cp_methodref.MethodRef = cp.get_constant(self.index)

    resolved_method = method_ref.resolved_method()
    if resolved_method.is_static():
      raise SystemExit('java.lang.IncompatibleClassChangeError')

    ref = frame.operand_stack.get_ref_from_top(
        resolved_method.arg_slot_count - 1)
    if ref == None:
      # hack
      if method_ref.name == 'println':
        _println(frame.operand_stack, method_ref.descriptor)
        return

      raise SystemExit('java.lang.NullPointerException')

    if (resolved_method.is_protected() and
            resolved_method.clazz.is_superclass_of(current_class) and
            resolved_method.clazz.get_package_name() != current_class.get_package_name() and
            ref.clazz != current_class and
            not ref.clazz.is_subclass_of(current_class)):
      raise SystemExit('java.lang.IllegalAccessError')

    # logging.info(f'{ref.clazz.super_class.methods=}, {method_ref.name}, {method_ref.descriptor}')
    # for m in ref.clazz.super_class.methods:
      # print(f'>>>>>>>>>{m.name=} {m.descriptor=}')
    method_to_be_invoked = lookup_method_in_class(
        ref.clazz, method_ref.name, method_ref.descriptor)
    if method_to_be_invoked == None or method_to_be_invoked.is_abstract():
      raise SystemExit('java.lang.AbstractMethodError')

    invoke_method(frame, method_to_be_invoked)


def _println(stack: OperandStack, descriptor: str):
  match descriptor:
    case '(Z)V':
      print(f'{stack.pop_int() != 0}')
    case '(C)V':
      print(f'{stack.pop_int()}')
    case '(B)V':
      print(f'{stack.pop_int()}')
    case '(S)V':
      print(f'{stack.pop_int()}')
    case '(I)V':
      print(f'{stack.pop_int()}')
    case '(F)V':
      print(f'{stack.pop_float()}')
    case '(J)V':
      print(f'{stack.pop_long()}')
    case '(D)V':
      print(f'{stack.pop_double()}')
    case '(Ljava/lang/String;)V':
      jstr = stack.pop_ref()
      py_str = pystring(jstr)
      print(py_str)
      
    case _:
      raise SystemExit(f'println: {descriptor}')
  stack.pop_ref()
