from .local_vars import LocalVars
from .operand_stack import OperandStack
from .heap.method import Method
# from .thread import Thread


class Frame:
  def __init__(self, thread , method:Method) -> None:
    self.lower: Frame = None
    self.local_vars = LocalVars(method.max_locals)
    self.operand_stack = OperandStack(method.max_stack)
    self.thread= thread
    self.method:Method = method
    
    self.next_pc: int = 0

  def set_next_pc(self, pc: int) -> None:
    self.next_pc = pc
  
  def method(self)-> Method:
    return self.method
