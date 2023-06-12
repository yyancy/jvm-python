

from jvm.rtda.frame import Frame
from jvm.rtda.heap import string_pool
from jvm.instructions.base.method_invoke_logic import invoke_method


def initialize(frame: Frame):
  class_loader = frame.method.clazz.loader
  jl_sys_class = class_loader.load_class('java/lang/System')
  init_sys_class = jl_sys_class.get_static_method(
      "initializeSystemClass", "()V")
  invoke_method(frame, init_sys_class)


def set_in0(frame: Frame):
  _vars = frame.local_vars
  _in = _vars.get_ref(0)

  sys_class = frame.method.clazz
  sys_class.set_ref_var("in", "Ljava/io/InputStream;", _in)


def set_out0(frame: Frame):
  _vars = frame.local_vars
  out = _vars.get_ref(0)

  sys_class = frame.method.clazz
  sys_class.set_ref_var('out', "Ljava/io/PrintStream;", out)


def set_err0(frame: Frame):
  _vars = frame.local_vars
  err = _vars.get_ref(0)

  sys_class = frame.method.clazz
  sys_class.set_ref_var("err", "Ljava/io/PrintStream;", err)
