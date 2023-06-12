

from jvm.instructions.base.class_init_logic import init_class
from jvm.instructions.base.method_invoke_logic import invoke_method
from jvm.native.java.lang.Class_helper import getSignatureStr, toByteArr, toClassArr
from jvm.rtda.frame import Frame, new_shim_frame
from jvm.rtda.heap import cls
from jvm.rtda.heap import string_pool
import logging

from jvm.rtda.operand_stack import OperandStack

def get_primitive_class(frame: Frame):
  name_obj = frame.local_vars.get_ref(0)
  name = string_pool.pystring(name_obj)
  loader = frame.method.clazz.loader
  clazz = loader.load_class(name).jclass
  frame.operand_stack.push_ref(clazz)


# private native String getName0();
def getName0(frame: Frame):
  this = frame.local_vars.get_this()
  clazz: cls.Class = this.extra
  name = clazz.java_name()
  name_obj = string_pool.jstring(clazz.loader, name)
  frame.operand_stack.push_ref(name_obj)
  

# private static native boolean desiredAssertionStatus0(Class<?> clazz);
def desired_assertion_status0(frame :Frame):
  frame.operand_stack.push_bool(False)


#  private static native Class<?> forName0(String name, boolean initialize,
#                                          ClassLoader loader,
#                                          Class<?> caller)
#      throws ClassNotFoundException;
#  (Ljava/lang/String;ZLjava/lang/ClassLoader;Ljava/lang/Class;)Ljava/lang/Class;
def forName0(frame :Frame):
  _vars = frame.local_vars
  jName = _vars.get_ref(0)
  initialize = _vars.get_bool(1)
  # jLoader = vars.GetRef(2)

  pyName = string_pool.pystring(jName)
  pyName = pyName.replace(".", "/", -1)
  goClass = frame.method.clazz.loader.load_class(pyName)
  if initialize and not goClass.init_started:
    #  undo forName0
    thread = frame.thread
    frame.set_next_pc(thread.pc)
    #  init class
    init_class(thread, goClass)
  else:
    stack = frame.operand_stack
    jClass = goClass.jclass

    stack.push_ref(jClass)
  

"""
Field(Class<?> declaringClass,
      String name,
      Class<?> type,
      int modifiers,
      int slot,
      String signature,
      byte[] annotations)
*/
"""
_fieldConstructorDescriptor = (
  "(Ljava/lang/Class;" 
  "Ljava/lang/String;" 
  "Ljava/lang/Class;" 
  "II" 
  "Ljava/lang/String;" 
  "[B)V"
)

#  private native Field[] getDeclaredFields0(boolean publicOnly);
#  (Z)[Ljava/lang/reflect/Field;
def getDeclaredFields0(frame :Frame):
  _vars = frame.local_vars
  classObj = _vars.get_this()
  publicOnly = _vars.get_bool(1)

  clazz:cls.Class = classObj.extra
  fields = clazz.get_fields(publicOnly)
  fieldCount = len(fields)

  classLoader = frame.method.clazz.loader
  fieldClass = classLoader.load_class("java/lang/reflect/Field")
  fieldArr = fieldClass.array_class().new_array(fieldCount)

  stack = frame.operand_stack
  stack.push_ref(fieldArr)

  if fieldCount > 0:
    thread = frame.thread
    fieldObjs = fieldArr.refs()
    fieldConstructor = fieldClass.get_constructor(_fieldConstructorDescriptor)
    for i, goField in enumerate(fields):
      fieldObj = fieldClass.new_object()
      fieldObj.extra = goField
      fieldObjs[i] = fieldObj

      ops = OperandStack(8)
      ops.push_ref(fieldObj)                                          #  this
      ops.push_ref(classObj)                                          #  declaringClass
      ops.push_ref(string_pool.jstring(classLoader, goField.name))         #  name
      ops.push_ref(goField.type().jclass)                           #  type
      ops.push_int(int(goField.access_flags))                      #  modifiers
      ops.push_int(int(goField.slot_id))                           #  slot
      ops.push_ref(getSignatureStr(classLoader, goField.signature)) #  signature
      ops.push_ref(toByteArr(classLoader, goField.annotation_data))  #  annotations

      shimFrame = new_shim_frame(thread, ops)
      thread.push_frame(shimFrame)

      #  init fieldObj
      invoke_method(shimFrame, fieldConstructor)
    
  

#  public native boolean isInterface();
#  ()Z
def isInterface(frame :Frame):
  _vars = frame.local_vars
  this = _vars.get_this()
  clazz = this.extra

  stack = frame.operand_stack
  stack.push_bool(clazz.is_interface())


#  public native boolean isPrimitive();
#  ()Z
def isPrimitive(frame :Frame):
  _vars = frame.local_vars
  this = _vars.get_this()
  clazz = this.extra

  stack = frame.operand_stack
  stack.push_bool(clazz.is_primitive())



#  public native boolean isAssignableFrom(Class<?> cls);
#  (Ljava/lang/Class;)Z
def isAssignableFrom(frame :Frame):
  _vars = frame.local_vars
  this = _vars.get_this()
  cls = _vars.get_ref(1)

  thisClass = this.extra
  clsClass = cls.extra
  ok = thisClass.is_assignable_from(clsClass)

  stack = frame.operand_stack
  stack.push_bool(ok)



#  public native int getModifiers();
#  ()I
def getModifiers(frame :Frame):
  _vars = frame.local_vars
  this = _vars.get_this()
  clazz = this.extra
  modifiers = clazz.access_flags

  stack = frame.operand_stack
  stack.push_int(modifiers)


#  public native Class<? super T> getSuperclass();
#  ()Ljava/lang/Class;
def getSuperclass(frame :Frame):
  _vars = frame.local_vars
  this = _vars.get_this()
  clazz = this.extra
  superClass = clazz.super_class

  stack = frame.operand_stack
  if superClass is not None:
    stack.push_ref(superClass.jclass)
  else:
    stack.push_ref(None)
  


#  private native Class<?>[] getInterfaces0();
#  ()[Ljava/lang/Class;
def getInterfaces0(frame :Frame):
  _vars = frame.local_vars
  this = _vars.get_this()
  clazz = this.extra
  interfaces = clazz.Interfaces()
  classArr = toClassArr(clazz.loader, interfaces)

  stack = frame.operand_stack
  stack.PushRef(classArr)


#  public native boolean isArray();
#  ()Z
def isArray(frame :Frame):
  _vars = frame.local_vars
  this = _vars.get_this()
  clazz = this.extra
  stack = frame.operand_stack
  stack.push_boolean(clazz.is_array())


#  public native Class<?> getComponentType();
#  ()Ljava/lang/Class;
def getComponentType(frame :Frame):
  _vars = frame.local_vars
  this = _vars.get_this()
  clazz = this.extra
  componentClass = clazz.component_class()
  componentClassObj = componentClass.jclass

  stack = frame.operand_stack
  stack.push_ref(componentClassObj)


#  public native boolean isAssignableFrom(Class<?> cls);
#  (Ljava/lang/Class;)Z
def isAssignableFrom(frame :Frame):
  _vars = frame.local_vars
  this = _vars.get_this()
  cls = _vars.get_ref(1)

  thisClass = this.extra
  clsClass = cls.extra
  ok = thisClass.is_assignable_from(clsClass)

  stack = frame.operand_stack
  stack.push_boolean(ok)

