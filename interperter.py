import logging
import time

import jvm.classfile.class_file as classfile
from jvm.rtda.frame import Frame
from jvm.rtda.heap.method import Method
import jvm.rtda.thread
from jvm.instructions.base.byte_reader import BytecodeReader
import jvm.instructions.base.instruction as instruction
import jvm.instructions.factory as factory

from objprint import op


def interpret(method: Method):
  thread = jvm.rtda.thread.Thread()
  frame = thread.new_frame(method)
  thread.push_frame(frame)
  try:
    loop(thread, method.code)
  except Exception as e:
    catch_err(e, frame)


def catch_err(e: Exception, frame: Frame):
  # op(frame.local_vars)
  # op(frame.operand_stack)
  logging.error(e)
  raise e


def loop(thread: jvm.rtda.thread.Thread, bytecode: bytes):
  frame = thread.pop_frame()
  reader = BytecodeReader()
  # logging.info(f"{bytecode=}")
  while True:
    pc = frame.next_pc
    thread.set_pc(pc)
    # decode
    reader.reset(bytecode, pc)
    opcode = reader.read_u8()
    inst: instruction.Instruction = factory.new_instruction(opcode)

    logging.info(f"{opcode=:0x} {pc=} {inst=}")
    # logging.info(frame.local_vars.slots)
    # logging.info(f'{frame.operand_stack.slots} {frame.operand_stack.size}')

    inst.fetch_operands(reader)
    frame.set_next_pc(reader.pc)

    # execute
    inst.execute(frame)
    # time.sleep(1)
