
from .cp_memberref import *
from .method import *
from .method_lookup import lookup_method_in_interfaces

from .cls import Class

class InterfaceMethodRef(MemberRef):

  def __init__(self, cp: ConstantPool, ref_info: MethodrefConstantInfo) -> None:
    super().__init__()
    self.cp = cp
    self.method: Method = None
    self.copy_memberref_info(ref_info)

  def resolved_interface_method(self) -> Method:
    if self.method == None:
      self.resolve_interface_method_ref()
    return self.method

  def resolve_interface_method_ref(self):
    d = self.cp.clazz
    c = self.resolved_class()
    if not c.is_interface():
      raise SystemExit('java.lang.IncompatibleClassChangeError')
    method = lookup_interface_method(c, self.name, self.descriptor)
    if method == None:
      raise SystemExit('java.lang.NoSuchMethodError')
    if not method.is_accessible_to(d):
      raise SystemExit('java.lang.IllegalAccessError')
    self.method = method


def lookup_interface_method(iface: Class, name: str, descriptor: str) -> Method:
  for method in iface.methods:
    if method.name == name and method.descriptor == descriptor:
      return method

  return lookup_method_in_interfaces(iface.interfaces, name, descriptor)
