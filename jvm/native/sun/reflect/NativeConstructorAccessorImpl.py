
#  private static native Object newInstance0(Constructor<?> c, Object[] os)
#  throws InstantiationException, IllegalArgumentException, InvocationTargetException;
#  (Ljava/lang/reflect/Constructor;[Ljava/lang/Object;)Ljava/lang/Object;
from jvm.instructions.base.class_init_logic import init_class
from jvm.instructions.base.method_invoke_logic import invoke_method
from jvm.rtda.frame import Frame, new_shim_frame
from jvm.rtda.heap.method import Method
from jvm.rtda.heap.object import Object
from jvm.rtda.operand_stack import OperandStack


def newInstance0(frame :Frame):
  _vars = frame.local_vars
  constructorObj = _vars.get_ref(0)
  argArrObj = _vars.get_ref(1)

  goConstructor = getGoConstructor(constructorObj)
  goClass = goConstructor.clazz
  if not goClass.init_started:
    frame.revert_next_pc()
    init_class(frame.thread, goClass)
    return
  

  obj = goClass.new_object()
  stack = frame.operand_stack
  stack.push_ref(obj)

  #  call <init>
  ops = convertArgs(obj, argArrObj, goConstructor)
  shimFrame = new_shim_frame(frame.thread, ops)
  frame.thread.push_frame(shimFrame)

  invoke_method(shimFrame, goConstructor)


def getGoMethod(methodObj :Object) ->Method:
  return _getGoMethod(methodObj, False)

def getGoConstructor(constructorObj :Object) ->Method:
  return _getGoMethod(constructorObj, True)

def _getGoMethod(methodObj :Object, isConstructor :bool) -> Method:
  extra = methodObj.extra
  if extra is not None:
    return extra


  if isConstructor:
    root = methodObj.get_refvar("root", "Ljava/lang/reflect/Constructor;")
  else:
    root = methodObj.get_refvar("root", "Ljava/lang/reflect/Method;")

  return root.extra
  


#  Object[] -> []interface{
def convertArgs(this:Object, argArr :Object, method :Method) ->OperandStack:
  if method.arg_slot_count == 0:
    return None
  

  #   argObjs = argArr.Refs()
  #   argTypes = method.ParsedDescriptor().ParameterTypes()

  ops = OperandStack(method.arg_slot_count)
  if not method.is_static():
    ops.push_ref(this)
  
  if method.arg_slot_count == 1 and not method.is_static():
    return ops
  

  #   for i, argType = range argTypes:
  #     argObj = argObjs[i]
  # 
  #     if len(argType) == 1:
  #       #  base type
  #       #  todo
  #       unboxed = box.Unbox(argObj, argType)
  #       args[i+j] = unboxed
  #       if argType.isLongOrDouble():
  #         j++
  #       
  #      else:
  #       args[i+j] = argObj
  #     
  #   

  return ops

