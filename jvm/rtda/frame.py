from jvm.rtda.heap import access_flag
from .local_vars import LocalVars
from .operand_stack import OperandStack
from .heap.method import Method
# from .thread import Thread


class Frame:
  def __init__(self, thread, method: Method) -> None:
    from jvm.rtda.thread import Thread
    self.thread: Thread = thread
    self.method: Method = method
    self.next_pc: int = 0
    if method is None:
      return
    self.lower: Frame = None
    self.local_vars = LocalVars(method.max_locals)
    self.operand_stack = OperandStack(method.max_stack)


  def set_next_pc(self, pc: int) -> None:
    self.next_pc = pc

  def method(self) -> Method:
    return self.method

  def revert_next_pc(self):
    self.next_pc = self.thread.pc


def shim_athrow_method()-> Method:
  from jvm.rtda.heap.cls import Class
  _shimClass  = Class()
  _shimClass.name = '~shim'
  
  _athrowCode = [0xbf]

  method = Method()
  method.access_flags = access_flag.ACC_STATIC
  method.name = "<athrow>"
  method.clazz = _shimClass
  method.code = _athrowCode
  
  return method
  

def shim_return_method()->Method:
  from jvm.rtda.heap.cls import Class
  _shimClass  = Class(None)
  _shimClass.name = '~shim'
  
  _returnCode = [0xb1]
  _athrowCode = [0xbf]

  method = Method()
  method.access_flags = access_flag.ACC_STATIC
  method.name = "<return>"
  method.clazz = _shimClass
  method.code = _returnCode
  method.descriptor='customs'
  
  return method
  


from jvm.rtda.thread import Thread
def new_shim_frame(thread: Thread,ops: OperandStack)-> Frame:
  frame = Frame(thread, None)
  frame.thread = thread
  frame.method = shim_return_method()
  frame.operand_stack = ops
  return frame