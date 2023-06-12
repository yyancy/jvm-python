


primitiveTypes ={
  "void":    "V",
  "boolean": "Z",
  "byte":    "B",
  "short":   "S",
  "int":     "I",
  "long":    "J",
  "char":    "C",
  "float":   "F",
  "double":  "D",
}


#  [XXX -> [[XXX
#  int -> [I
#  XXX -> [LXXX;
def getArrayClassName(className:str) -> str:
  return f"[{toDescriptor(className)}"


#  [[XXX -> [XXX
#  [LXXX; -> XXX
#  [I -> int
def getComponentClassName(className:str)->str:
  if className[0] == '[':
    componentTypeDescriptor = className[1:]
    return toClassName(componentTypeDescriptor)
  
  raise SystemExit(f"Not array: {className}")


#  [XXX => [XXX
#  int  => I
#  XXX  => LXXX;
def toDescriptor(className:str) -> str:
  if className[0] == '[':
    #  array
    return className

  d = primitiveTypes.get(className)
  return d if d is not None else f"L{className};"
  


#  [XXX  => [XXX
#  LXXX; => XXX
#  I     => int
def toClassName(descriptor:str) -> str:
  if descriptor[0] == '[':
    #  array
    return descriptor

  if descriptor[0] == 'L':
    #  object
    return descriptor[1:-1]

  for className, d in primitiveTypes.items():
    if d == descriptor:
      #  primitive
      return className

  raise SystemExit(f"Invalid descriptor: {descriptor}")
