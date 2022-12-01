from .entry import Entry
from .entry import Err
import zipfile
import os.path

class ZipEntry(Entry):
  def __init__(self, path:str) -> None:
     super().__init__()
     self.abs_path = path
     
     
  def read_class(self, class_name: str) -> tuple[bytes,Entry, Err]:
    zip = zipfile.ZipFile(self.abs_path)
    with zip.open(class_name) as f:
      b = f.read()
    return b, self, None


  def __str__(self) -> str:
    return self.abs_path


def new_zip_entry(path: str)-> ZipEntry:
  path = os.path.abspath(path)
  return ZipEntry(path)