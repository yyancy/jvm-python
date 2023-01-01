
from ..base.instruction import NoOperandsInstuction
from rtda.frame import Frame


class ACONST_NULL(NoOperandsInstuction):
  def __init__(self) -> None:
    super().__init__()

  def execute(self, frame: Frame):
    frame.operand_stack.push_ref(None)


class DCONST_0(NoOperandsInstuction):
  def __init__(self) -> None:
    super().__init__()

  def execute(self, frame: Frame):
    frame.operand_stack.push_double(0.0)


class DCONST_1(NoOperandsInstuction):
  def __init__(self) -> None:
    super().__init__()

  def execute(self, frame: Frame):
    frame.operand_stack.push_double(1.0)


class FCONST_0(NoOperandsInstuction):
  def __init__(self) -> None:
    super().__init__()

  def execute(self, frame: Frame):
    frame.operand_stack.push_float(0.0)


class FCONST_1(NoOperandsInstuction):
  def __init__(self) -> None:
    super().__init__()

  def execute(self, frame: Frame):
    frame.operand_stack.push_float(1.0)


class FCONST_2(NoOperandsInstuction):
  def __init__(self) -> None:
    super().__init__()

  def execute(self, frame: Frame):
    frame.operand_stack.push_float(2.0)


class ICONST_M1(NoOperandsInstuction):
  def __init__(self) -> None:
    super().__init__()

  def execute(self, frame: Frame):
    frame.operand_stack.push_int(-1)


class ICONST_0(NoOperandsInstuction):
  def __init__(self) -> None:
    super().__init__()

  def execute(self, frame: Frame):
    frame.operand_stack.push_int(0)


class ICONST_1(NoOperandsInstuction):
  def __init__(self) -> None:
    super().__init__()

  def execute(self, frame: Frame):
    frame.operand_stack.push_int(1)


class ICONST_2(NoOperandsInstuction):
  def __init__(self) -> None:
    super().__init__()

  def execute(self, frame: Frame):
    frame.operand_stack.push_int(2)


class ICONST_3(NoOperandsInstuction):
  def __init__(self) -> None:
    super().__init__()

  def execute(self, frame: Frame):
    frame.operand_stack.push_int(3)


class ICONST_4(NoOperandsInstuction):
  def __init__(self) -> None:
    super().__init__()

  def execute(self, frame: Frame):
    frame.operand_stack.push_int(4)


class ICONST_5(NoOperandsInstuction):
  def __init__(self) -> None:
    super().__init__()

  def execute(self, frame: Frame):
    frame.operand_stack.push_int(5)


class LCONST_0(NoOperandsInstuction):
  def __init__(self) -> None:
    super().__init__()

  def execute(self, frame: Frame):
    frame.operand_stack.push_long(0)


class LCONST_1(NoOperandsInstuction):
  def __init__(self) -> None:
    super().__init__()

  def execute(self, frame: Frame):
    frame.operand_stack.push_long(1)
