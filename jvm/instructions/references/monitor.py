
from ..base.instruction import *

from jvm.rtda.frame import Frame


#  Enter monitor for object
class MONITOR_ENTER(NoOperandsInstuction):
  def execute(self, frame: Frame):
    ref = frame.operand_stack.pop_ref()
    if ref is None:
      raise SystemExit('java.lang.NullPointerException')


#  Exit monitor for object
class MONITOR_EXIT(NoOperandsInstuction):
  def execute(self, frame: Frame):
    ref = frame.operand_stack.pop_ref()
    if ref is None:
      raise SystemExit('java.lang.NullPointerException')
