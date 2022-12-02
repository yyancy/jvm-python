from .entry import Entry
from .entry import Err
import os.path
import logging

class DirEntry(Entry):
  def __init__(self, path:str) -> None:
     super().__init__()
     self.abs_path = path
     

  def read_class(self, class_name: str) -> tuple[bytes,Entry, Err]:
    filename = os.path.join(self.abs_path, class_name)
    try:
        with open(filename,'rb') as f:
            b = f.read()
    except Exception as e:
        logging.error(f"could not find class: {e}")
        return None, None, e
    return b, self, e


  def __str__(self) -> str:
    return self.abs_path


def new_dir_entry(path: str)-> DirEntry:
  path = os.path.abspath(path)
  return DirEntry(path)