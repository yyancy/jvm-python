import logging
import time

import jvm.classfile.class_file as classfile
from jvm.rtda.frame import Frame
from jvm.rtda.heap.class_loader import ClassLoader
from jvm.rtda.heap.method import Method
from jvm.rtda.heap.object import Object
from jvm.rtda.heap.string_pool import jstring
import jvm.rtda.thread
from jvm.instructions.base.byte_reader import BytecodeReader
import jvm.instructions.base.instruction as instruction
import jvm.instructions.factory as factory

from objprint import op


def create_args_array(loader: ClassLoader, args: list[str]) -> Object:
  string_class = loader.load_class('java/lang/String')
  args_arr = string_class.array_class().new_array(len(args))
  jargs = args_arr.refs()
  for i in range(len(args)):
    jargs[i] = jstring(loader, args[i])
  return args_arr


def interpret(method: Method, log_inst: bool, args: list[str]):
  thread = jvm.rtda.thread.Thread()
  frame = thread.new_frame(method)
  thread.push_frame(frame)
  jargs = create_args_array(method.clazz.loader, args)
  frame.local_vars.set_ref(0, jargs)
  try:
    loop(thread, log_inst)
  except Exception as e:
    catch_err(e, frame, thread)


def catch_err(e: Exception, frame: Frame, thread: jvm.rtda.thread.Thread):
  # op(frame.local_vars)
  # op(frame.operand_stack)
  log_frames(thread)
  raise e


def log_frames(thread: jvm.rtda.thread.Thread):
  while not thread.is_stack_empty():
    frame = thread.pop_frame()
    method = frame.method
    class_name = method.clazz.name
    print(
        f'>> pc:{frame.next_pc} {class_name=} {method.name=} {method.descriptor=}')


def log_instruction(frame: Frame, inst: instruction.Instruction):
  method = frame.method
  class_name = method.clazz.name
  method_name = method.name
  pc = frame.thread.pc

  print(f'{class_name=} {method_name=} {pc=} {inst=}')


def loop(thread: jvm.rtda.thread.Thread, log_inst: bool):
  reader = BytecodeReader()
  # logging.info(f"{bytecode=}")
  while True:
    frame = thread.current_frame()
    pc = frame.next_pc
    thread.set_pc(pc)
    # decode
    reader.reset(frame.method.code, pc)
    opcode = reader.read_u8()
    inst: instruction.Instruction = factory.new_instruction(opcode)

    # logging.info(f"{opcode=:0x} {pc=} {inst=}")
    # logging.info(frame.local_vars.slots)
    # logging.info(f'{frame.operand_stack.slots} {frame.operand_stack.size}')

    inst.fetch_operands(reader)
    frame.set_next_pc(reader.pc)
    if (log_inst):
      log_instruction(frame, inst)

    # execute
    inst.execute(frame)
    if thread.is_stack_empty():
      break
    # time.sleep(1)
