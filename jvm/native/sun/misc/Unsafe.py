
from jvm.rtda.frame import Frame
from jvm.rtda.heap.object import Object
from jvm.rtda.heap.slots import Slots


miscUnsafe = "sun/misc/Unsafe"
#  public native int arrayBaseOffset(Class<?> type);
#  (Ljava/lang/Class;)I


def arrayBaseOffset(frame: Frame):
  stack = frame.operand_stack
  stack.push_int(0)  # todo


#  public native int arrayIndexScale(Class<?> type);
#  (Ljava/lang/Class;)I
def arrayIndexScale(frame: Frame):
  stack = frame.operand_stack
  stack.push_int(1)  # todo


#  public native int addressSize();
#  ()I
def addressSize(frame: Frame):
  #  vars = frame.local_vars
  #  vars.GetRef(0) #  this

  stack = frame.operand_stack
  stack.push_int(8)  # todo unsafe.Sizeof(int)


#  public native long objectFieldOffset(Field field);
#  (Ljava/lang/reflect/Field;)J
def objectFieldOffset(frame: Frame):
  _vars = frame.local_vars
  jField = _vars.get_ref(1)

  offset = jField.get_intvar("slot", "I")

  stack = frame.operand_stack
  stack.PushLong(int(offset))


#  public final native boolean compareAndSwapObject(Object o, long offset, Object expected, Object x)
#  (Ljava/lang/Object;JLjava/lang/Object;Ljava/lang/Object;)Z
def compareAndSwapObject(frame: Frame):
  _vars = frame.local_vars
  obj = _vars.get_ref(1)
  fields = obj.data
  offset = _vars.get_long(2)
  expected = _vars.get_ref(4)
  newVal = _vars.get_ref(5)

  #  todo
  match(fields):
    case Slots() as anys:
        #  object
      swapped = _casObj(obj, anys, offset, expected, newVal)
      frame.operand_stack.push_bool(swapped)
    case list() as objs:
      #  ref[]
      if all(isinstance(n, Object) for n in objs):
        swapped = _casArr(objs, offset, expected, newVal)
        frame.operand_stack.push_bool(swapped)
    case _:
      #  todo
      raise SystemExit("todo: compareAndSwapObject!")


def _casObj(obj: Object, fields: Slots, offset: int, expected: Object, newVal: Object) -> bool:
  current = fields.get_ref(offset)
  if current == expected:
    fields.set_ref(offset, newVal)
    return True
  else:
    return False


def _casArr(objs: list[Object], offset: int, expected, newVal: Object) -> bool:
  current = objs[offset]
  if current == expected:
    objs[offset] = newVal
    return True
  else:
    return False


#  public native boolean getInt(Object o, long offset);
#  (Ljava/lang/Object;J)I
def getInt(frame: Frame):
  _vars = frame.local_vars
  fields = _vars.get_ref(1).data
  offset = _vars.get_long(2)

  stack = frame.operand_stack
  match(fields):
    case Slots() as slots:
      #  object
      stack.push_int(slots.get_int(offset))
    case list() as shorts:
      #  int[]
      if all(isinstance(n, int) for n in shorts):
        stack.push_int(shorts[offset])
    case _:
      raise SystemExit("getInt!")


#  public final native boolean compareAndSwapInt(Object o, long offset, int expected, int x);
#  (Ljava/lang/Object;JII)Z
def compareAndSwapInt(frame: Frame):
  _vars = frame.local_vars
  fields = _vars.get_ref(1).data
  offset = _vars.get_long(2)
  expected = _vars.get_int(4)
  newVal = _vars.get_int(5)

  match(fields):
    case Slots() as slots:
      #  object
      oldVal = slots.get_int(offset)
      if oldVal == expected:
        slots.set_int(offset, newVal)
        frame.operand_stack.push_bool(True)
      else:
        frame.operand_stack.push_bool(False)
    case list() as ints:
        #  int[]
      if all(isinstance(n, int) for n in ints):
        oldVal = ints[offset]
        if oldVal == expected:
          ints[offset] = newVal
          frame.operand_stack.push_bool(True)
        else:
          frame.operand_stack.push_bool(False)

    case _:
        #  todo
      raise SystemExit("todo: compareAndSwapInt!")


#  public native Object getObject(Object o, long offset);
#  (Ljava/lang/Object;J)Ljava/lang/Object;
def getObject(frame: Frame):
  _vars = frame.local_vars
  fields = _vars.get_ref(1).data
  offset = _vars.get_long(2)

  match(fields):
    case Slots() as anys:
      #  object
      x = anys.get_ref(offset)
      frame.operand_stack.push_ref(x)
    case list() as objs:
      #  ref[]
      if all(isinstance(n, Object) for n in objs):
        #  ref[]
        x = objs[offset]
      frame.operand_stack.push_ref(x)
    case _:
      raise SystemExit("getObject!")


#  public final native boolean compareAndSwapLong(Object o, long offset, long expected, long x);
#  (Ljava/lang/Object;JJJ)Z
def compareAndSwapLong(frame: Frame):
  _vars = frame.local_vars
  fields = _vars.get_ref(1).data
  offset = _vars.get_long(2)
  expected = _vars.get_long(4)
  newVal = _vars.get_long(6)

  match(fields):
    case Slots() as slots:
      #  object
      oldVal = slots.get_long(offset)
      if oldVal == expected:
        slots.set_long(offset, newVal)
        frame.operand_stack.push_bool(True)
      else:
        frame.operand_stack.push_bool(False)

    case list() as longs:
      if all(isinstance(n, int) for n in longs):
        #  long[]
        oldVal = longs[offset]
        if oldVal == expected:
          longs[offset] = newVal
          frame.operand_stack.push_bool(True)
        else:
          frame.operand_stack.push_bool(False)
    case _:
        #  todo
      raise SystemExit("todo: compareAndSwapLong!")
