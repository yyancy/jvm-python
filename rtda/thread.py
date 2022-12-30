
from .frame import Frame


class Stack:
  def __init__(self, max_size: int) -> None:
    self.max_size = max_size
    self.size = 0
    self._top: Frame

  def push(self, frame: Frame):
    if self.size > self.max_size:
      raise Exception("java.lang.StackOverflowError")
    if self._top != None:
      frame.lower = self._top

    self._top = frame
    self.size += 1

  def pop(self) -> Frame:
    if self.size <= 0:
      raise Exception("There is no more frame")
    top = self._top
    self._top = self._top.lower
    top.lower = None
    self.size -= 1
    return top

  def top(self) -> Frame:
    if self.size <= 0:
      raise Exception("There is no more frame")
    return self._top


class Thread:
  def __init__(self) -> None:
    self.pc: int
    self.stack: Stack = Stack(1024)

  @property.setter
  def set_pc(self, v: int) -> None:
    self.pc = v

  def push_frame(self, frame: Frame):
    self.stack.push(frame)

  def pop_frame(self,) -> Frame:
    return self.stack.pop()

  def current_frame(self,) -> Frame:
    return self.stack.top()

  def new_frame(self, max_locals: int, max_stacks: int) -> Frame:
    return Frame(self, max_locals, max_stacks)
