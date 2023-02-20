from __future__ import annotations
import os
path_list_sep = os.pathsep


class Err(Exception):
  def __init__(self, *args: object) -> None:
     super().__init__(*args)
  
# class Entry:
#   pass

class Entry:
    def read_class(self, class_name: str) -> tuple[bytes,Entry, Err]:
        pass
    def __str__(self) -> str:
        pass







    