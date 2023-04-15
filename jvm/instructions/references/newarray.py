

import types
from jvm.instructions.base.byte_reader import BytecodeReader
from jvm.instructions.base.instruction import Instruction
from jvm.rtda.frame import Frame
from jvm.rtda.heap.class_loader import ClassLoader
from jvm.rtda.heap.cls import Class

single = types.SimpleNamespace()
single.AT_BOOLEAN = 4
single.AT_CHAR = 5
single.AT_FLOAT = 6
single.AT_DOUBLE = 7
single.AT_BYTE = 8
single.AT_SHORT = 9
single.AT_INT = 10
single.AT_LONG = 11


class NEW_ARRAY(Instruction):
  def __init__(self) -> None:
    super().__init__()
    self.atype = 0

  def fetch_operands(self, reader: BytecodeReader):
    
    self.atype = reader.read_u8()
    
    

  def execute(self, frame: Frame):
    stack = frame.operand_stack
    count = stack.pop_int()
    if count < 0:
      raise SystemExit(f'java.lang.NegativeArraySizeException')
    class_loader = frame.method.clazz.loader
    arr_class = get_primitive_array_class(class_loader, self.atype)
    arr = arr_class.new_array(count)
    stack.push_ref(arr)


def get_primitive_array_class(loader: ClassLoader, atype: int) -> Class:
  match atype:
    case single.AT_BOOLEAN:
      return loader.load_class('[z')
    case single.AT_BYTE:
      return loader.load_class('[B')
    case single.AT_CHAR:
      return loader.load_class('[C')
    case single.AT_SHORT:
      return loader.load_class('[S')
    case single.AT_INT:
      return loader.load_class('[I')
    case single.AT_LONG:
      return loader.load_class('[L')
    case single.AT_FLOAT:
      return loader.load_class('[F')
    case single.AT_DOUBLE:
      return loader.load_class('[D')
    case _:
      raise SystemExit(f'Invalid atype!')
