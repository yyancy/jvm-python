from ..base.instruction import NoOperandsInstuction


class NOP(NoOperandsInstuction):
  def __init__(self) -> None:
    super().__init__()
