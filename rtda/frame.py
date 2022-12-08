from .local_vars import LocalVars
from .operand_stack import OperandStack


class Frame:
  def __init__(self, max_locals, max_stack: int) -> None:
    self.lower: Frame
    self.local_vars = LocalVars(max_locals)
    self.operand_stack = OperandStack(max_stack)
