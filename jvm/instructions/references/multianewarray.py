from jvm.instructions.base.byte_reader import BytecodeReader
from jvm.instructions.base.instruction import Instruction, NoOperandsInstuction
from jvm.rtda.frame import Frame
from jvm.rtda.heap.cls import Class
from jvm.rtda.heap.object import Object
from jvm.rtda.heap.cp_classref import ClassRef
from jvm.common.cons import *
from jvm.rtda.operand_stack import OperandStack


class MULTI_ANEW_ARRAY(Instruction):
  def __init__(self) -> None:
    self.index: uint16
    self.dimensions: uint8

  def fetch_operands(self, reader: BytecodeReader):
    self.index: uint16 = reader.read_u16()
    self.dimensions: uint8 = reader.read_u8()

  def execute(self, frame: Frame):
    cp = frame.method.clazz.constant_pool
    class_ref: ClassRef = cp.get_constant(self.index)
    arr_class = class_ref.resolved_class()
    stack = frame.operand_stack
    counts = pop_and_check_counts(stack, self.dimensions)
    arr = new_multi_dimensional_array(counts, arr_class)
    stack.push_ref(arr)

def new_multi_dimensional_array(counts: list[int], arr_class:Class)-> Object:
  count = counts[0]
  arr = arr_class.new_array(count)
  if len(counts) > 1:
    refs = arr.refs()
    for i in range(len(refs)):
      refs[i] = new_multi_dimensional_array(counts[1:], arr_class.component_class())

  

def pop_and_check_counts(stack: OperandStack, dimensions: int) -> list[int]:
  counts = [None] * dimensions
  for i in range(dimensions-1, -1, - 1):
    counts[i] = stack.pop_int()
    if counts[i] < 0:
      raise SystemExit(f'java.lang.NegativeArraySizeException')

  return counts
