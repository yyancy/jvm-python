
from jvm.classfile.class_file import ExceptionTableEntry
from jvm.rtda.heap.constant_pool import ConstantPool
from jvm.rtda.heap.cp_classref import ClassRef
from jvm.rtda.heap import cls

class ExceptionHandler:
  def __init__(self) -> None:
    self.start_pc = 0
    self.end_pc = 0
    self.handler_pc = 0
    self.catch_type: ClassRef = None


class ExceptionTable:
  def __init__(self, entries: list[ExceptionTableEntry], cp: ConstantPool) -> None:
    self.handlers: list[ExceptionHandler] = [None]*len(entries)
    for i, entry in enumerate(entries):
      handler = ExceptionHandler()
      handler.start_pc = entry.start_pc
      handler.end_pc = entry.end_pc
      handler.handler_pc = entry.handler_pc
      handler.catch_type = get_catch_type(entry.catch_type, cp)
      self.handlers[i] = handler

  def find_exception_handler(self, ex_class: cls.Class, pc: int) -> ExceptionHandler:
    for handler in self.handlers:
      if pc >= handler.start_pc and pc < handler.end_pc:
        if handler.catch_type is None:
          return handler  # catch all

        catch_class = handler.catch_type.resolved_class()
        if catch_class == ex_class or catch_class.is_superclass_of(ex_class):
          return handler
    return None


def get_catch_type(index: int, cp: ConstantPool) -> ClassRef:
  return None if index == 0 else cp.get_constant(index)
