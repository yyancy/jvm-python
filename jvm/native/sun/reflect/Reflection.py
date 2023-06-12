
from jvm.rtda.frame import Frame


#  public static native Class<?> getCallerClass();
#  ()Ljava/lang/Class;
def getCallerClass(frame :Frame):
	#  top0 is sun/reflect/Reflection
	#  top1 is the caller of getCallerClass()
	#  top2 is the caller of method
  callerFrame = frame.thread.get_frames()[2] # todo
  callerClass = callerFrame.method.clazz.jclass
  frame.operand_stack.push_ref(callerClass)
  

#  public static native int getClassAccessFlags(Class<?> type);
#  (Ljava/lang/Class;)I
def getClassAccessFlags(frame :Frame):
	_vars = frame.local_vars
	_type = _vars.get_ref(0)

	pyClass = _type.extra
	flags = pyClass.access_flags

	stack = frame.operand_stack
	stack.push_int(flags)