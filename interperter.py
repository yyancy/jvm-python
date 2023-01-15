import logging
import time

import classfile.class_file as classfile
from rtda.frame import Frame
import rtda.thread
from instructions.base.byte_reader import BytecodeReader
import instructions.base.instruction as instruction
import instructions.factory as factory

from objprint import op


def interpret(methodinfo: classfile.MemberInfo):
  code_attr = methodinfo.code_attribute()
  max_locals = code_attr.max_locals
  max_stacks = code_attr.max_stacks
  bytecode = code_attr.codes
  thread = rtda.thread.Thread()
  frame = thread.new_frame(max_locals, max_stacks)
  thread.push_frame(frame)
  try:
    loop(thread, bytecode)
  except Exception as e:
    catch_err(e, frame)


def catch_err(e: Exception, frame: Frame):
  op(frame.local_vars)
  op(frame.operand_stack)
  logging.error(e)


def loop(thread: rtda.thread.Thread, bytecode: bytes):
  frame = thread.pop_frame()
  reader = BytecodeReader()
  logging.info(f"{bytecode=}")
  while True:
    pc = frame.next_pc
    thread.set_pc(pc)
    # decode
    reader.reset(bytecode, pc)
    opcode = reader.read_u8()
    inst: instruction.Instruction = factory.new_instruction(opcode)

    logging.info(f"{opcode=:0x} {pc=} {inst=}")

    inst.fetch_operands(reader)
    frame.set_next_pc(reader.pc)

    # execute
    inst.execute(frame)
    # time.sleep(1)
