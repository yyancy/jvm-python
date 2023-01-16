from .local_vars import LocalVars
from .operand_stack import OperandStack
# from .thread import Thread


class Frame:
  def __init__(self, thread ,  max_locals: int, max_stack: int) -> None:
    self.lower: Frame = None
    self.local_vars = LocalVars(max_locals)
    self.operand_stack = OperandStack(max_stack)
    self.thread= thread
    
    self.next_pc: int = 0

  def set_next_pc(self, pc: int) -> None:
    self.next_pc = pc
