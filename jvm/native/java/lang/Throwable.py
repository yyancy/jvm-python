

from dataclasses import dataclass, fields
from jvm.rtda.frame import Frame
from jvm.rtda.heap.object import Object
from jvm.rtda.thread import Thread
from jvm.rtda.heap import cls


@dataclass
class StackTraceElement:
  file_name: str
  class_name: str
  method_name: str
  line_number: int

  def __repr__(self):
    return f'{self.class_name}.{self.method_name}({self.file_name}:{self.line_number})'


def fill_in_stack_trace(frame: Frame):
  # assert False, f'to be implemented'
  this = frame.local_vars.get_this()
  frame.operand_stack.push_ref(this)
  stes = create_stack_trace_elements(this, frame.thread)
  this.extra = stes


def distance_to_object(clazz: cls.Class) -> int:
  distance = 0
  c = clazz.super_class
  while c is not None:
    distance += 1
    c = c.super_class
  return distance


def create_stack_trace_element(frame: Frame) -> StackTraceElement:
  method = frame.method
  clazz = method.clazz
  return StackTraceElement(file_name=clazz.source_file,
                           class_name=clazz.java_name(),
                           method_name=method.name,
                           line_number=method.get_line_number(frame.next_pc-1))


def create_stack_trace_elements(tobj: Object, thread: Thread) -> list[StackTraceElement]:
  skip = distance_to_object(tobj.clazz) + 2
  frames = thread.get_frames()[skip:]
  stes = [None] * len(frames)
  for i, frame in enumerate(frames):
    stes[i] = create_stack_trace_element(frame)
  return stes
