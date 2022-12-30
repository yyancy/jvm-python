
from base.instruction import *

from rtda.frame import Frame


def rshift(val, n): return (val % 0x100000000) >> n
# int左移


class ISHL(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    v2 = stack.push_int()
    v1 = stack.push_int()
    s = v2 & 0x1f
    result = v1 << s
    stack.push_int(result)
# int 算术右移动(有符号位)


class ISHR(NoOperandsInstuction):
  pass
# int 逻辑右移动


class IUSHR(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    v2 = stack.push_int()
    v1 = stack.push_int()
    s = v2 & 0x1f
    result = rshift(v1, s)
    stack.push_int(result)
# long左移


class LSHL(NoOperandsInstuction):
  pass
# long 算术右移动(有符号位)


class LSHR(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    v2 = stack.push_int()
    v1 = stack.push_long()
    s = v2 & 0x3f
    result = v1 >> s
    stack.push_long(result)
# long 逻辑右移动


class LUSHR(NoOperandsInstuction):
  pass
