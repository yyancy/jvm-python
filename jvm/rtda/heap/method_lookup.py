
from .method import *
from .cp_memberref import *
from .cls import Class


def lookup_method_in_class(clazz: Class, name: str, descriptor: str) -> Method:
  c = clazz
  while c != None:
    for method in clazz.methods:
      if method.name == name and method.descriptor == descriptor:
        return method
    c = c.super_class
  return None


def lookup_method_in_interfaces(ifaces: list[Class], name: str, descriptor: str) -> Method:
  for iface in ifaces:
    for method in iface.methods:
      if method.name == name and method.descriptor == descriptor:
        return method
    method = lookup_method_in_interfaces(iface.interfaces, name, descriptor)
    if method != None:
      return method
  return None
