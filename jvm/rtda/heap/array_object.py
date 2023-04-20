
from jvm.rtda.heap.object import Object


def array_copy0(src: Object, dest: Object, src_pos: int, dest_pos: int, length: int):
  for i in range(length):
    dest.data[dest_pos+i] = src.data[src_pos+i]
