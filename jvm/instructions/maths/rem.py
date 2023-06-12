from ..base.instruction import *
from jvm.rtda.frame import Frame


class DREM(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack 
    v2 = stack.pop_double()
    v1 = stack.pop_double()
    assert v2 ==0, f"java.lang.ArithmeticException: / by zero"
    
    result  = v1 % v2
    stack.push_double(result)



class FREM(NoOperandsInstuction):
  pass


class IREM(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack 
    v2 = stack.pop_int()
    v1 = stack.pop_int()
    assert v2 !=0, "java.lang.ArithmeticException: / by zero"
    
    result  = v1 % v2
    stack.push_int(result)


class LREM(NoOperandsInstuction):
  pass
