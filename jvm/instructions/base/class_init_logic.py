

from jvm.rtda.heap.cls import Class
from jvm.rtda.thread import Thread


def init_class(thread: Thread, clazz: Class):
  clazz.start_init()
  schedule_clinit(thread, clazz)
  init_superclass(thread, clazz)


def schedule_clinit(thread: Thread, clazz: Class):
  clinit = clazz.get_clinit_method()
  if clinit != None:
    new_frame = thread.new_frame(clinit)
    thread.push_frame(new_frame)


def init_superclass(thread: Thread, clazz: Class):
  if not clazz.is_interface():
    superclass = clazz.super_class
    if superclass != None and not superclass.init_started:
      init_class(thread, superclass)
