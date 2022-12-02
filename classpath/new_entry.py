from .entry import *
from .entry_dir import new_dir_entry

def new_entry(path: str)-> Entry:
    if path_list_sep in path:
      from .entry_composite import new_composite_entry
      return new_composite_entry(path)
    if path.endswith("*"):
        from .entry_wildcard import new_wildcard_entry
        return new_wildcard_entry(path)

    if path.endswith((".jar",".JAR",".zip",".ZIP")):
      from .entry_zip import new_zip_entry
      return new_zip_entry(path)
    
    return new_dir_entry(path)
  