
from jvm.rtda.heap.method import Method


from jvm.rtda.frame import Frame


class Stack:
  def __init__(self, max_size: int) -> None:
    self.max_size = max_size
    self.size = 0
    self._top: Frame = None

  def get_frames(self) -> list[Frame]:
    frames = []
    frame = self._top
    while frame is not None:
      frames.append(frame)
      frame = frame.lower
    return frames

  def clear(self):
    while not self.is_empty():
      self.pop()

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

  def is_empty(self) -> bool:
    return self._top == None


class Thread:
  def __init__(self) -> None:
    self.pc: int
    self.stack: Stack = Stack(1024)

  def get_frames(self) -> list[Frame]:
    return self.stack.get_frames()

  def clear_stack(self):
    self.stack.clear()

  def set_pc(self, v: int) -> None:
    self.pc = v

  def push_frame(self, frame: Frame):
    self.stack.push(frame)

  def pop_frame(self,) -> Frame:
    return self.stack.pop()

  def current_frame(self,) -> Frame:
    return self.stack.top()

  def top_frame(self,) -> Frame:
    return self.stack.top()

  def new_frame(self, method: Method) -> Frame:
    return Frame(self, method)

  def is_stack_empty(self) -> bool:
    return self.stack.is_empty()
