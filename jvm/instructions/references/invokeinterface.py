
import logging
from jvm.instructions.base.byte_reader import BytecodeReader
from jvm.instructions.base.instruction import Instruction
from jvm.instructions.base.method_invoke_logic import invoke_method
from jvm.rtda.frame import Frame
from jvm.rtda.heap.cp_interface_methodref import InterfaceMethodRef
from jvm.rtda.heap.method_lookup import lookup_method_in_class


class INVOKE_INTERFACE(Instruction):
  def fetch_operands(self, reader: BytecodeReader):
    self.index = reader.read_u16()
    reader.read_u8()  # count
    reader.read_u8()  # must be zero

  def execute(self, frame: Frame):
    cp = frame.method.clazz.constant_pool
    method_ref: InterfaceMethodRef = cp.get_constant(self.index)
    resolved_method = method_ref.resolved_interface_method()
    logging.info(f'{method_ref.name} {resolved_method.arg_slot_count=}')
    if resolved_method.is_static() or resolved_method.is_private():
      raise SystemExit(f'java.lang.IncompatibleClassChangeError')
    ref = frame.operand_stack.get_ref_from_top(
        resolved_method.arg_slot_count - 1)
    if ref == None:
      logging.info('coming here')
      raise SystemExit('java.lang.NullPointerException')
    if not ref.clazz.is_implements(method_ref.resolved_class()):
      raise SystemExit('java.lang.IncompatibleClassChangeError')
    method_to_be_invoked = lookup_method_in_class(
        ref.clazz, method_ref.name, method_ref.descriptor)
    if method_to_be_invoked == None or method_to_be_invoked.is_abstract():
      raise SystemExit('java.lang.AbstractMethodError')
    if not method_to_be_invoked.is_public():
      raise SystemExit('java.lang.IllegalAccessError')

    invoke_method(frame, method_to_be_invoked)
