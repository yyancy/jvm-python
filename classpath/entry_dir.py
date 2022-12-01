from .entry import Entry
from .entry import Err
import os.path

class DirEntry(Entry):
  def __init__(self, path:str) -> None:
     super().__init__()
     self.abs_path = path
     

  def read_class(self, class_name: str) -> tuple[bytes,Entry, Err]:
    filename = os.path.join(self.abs_path, class_name)
    with open(filename,'rb') as f:
      b = f.read()
    return b, self, None


  def __str__(self) -> str:
    return self.abs_path


def new_dir_entry(path: str)-> DirEntry:
  path = os.path.abspath(path)
  return DirEntry(path)