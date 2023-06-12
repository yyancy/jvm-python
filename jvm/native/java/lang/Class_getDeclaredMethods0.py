

# /*
# Method(Class<?> declaringClass,
#        String name,
#        Class<?>[] parameterTypes,
#        Class<?> returnType,
#        Class<?>[] checkedExceptions,
#        int modifiers,
#        int slot,
#        String signature,
#        byte[] annotations,
#        byte[] parameterAnnotations,
#        byte[] annotationDefault)
# */
from jvm.instructions.base.method_invoke_logic import invoke_method
from jvm.native.java.lang.Class_helper import getSignatureStr, toByteArr, toClassArr
from jvm.rtda.frame import Frame, new_shim_frame
from jvm.rtda.heap import string_pool
from jvm.rtda.operand_stack import OperandStack


_methodConstructorDescriptor = (
	"(Ljava/lang/Class;" +
	"Ljava/lang/String;" +
	"[Ljava/lang/Class;" +
	"Ljava/lang/Class;" +
	"[Ljava/lang/Class;" +
	"II" +
	"Ljava/lang/String;" +
	"[B[B[B)V"
)
#  private native Method[] getDeclaredMethods0(boolean publicOnly);
#  (Z)[Ljava/lang/reflect/Method;
def getDeclaredMethods0(frame :Frame):
	_vars = frame.local_vars
	classObj = _vars.get_this()
	publicOnly = _vars.get_boolean(1)

	clazz = classObj.extra
	methods = clazz.get_methods(publicOnly)
	methodCount = len(methods)

	classLoader = clazz.loader
	methodClass = classLoader.load_class("java/lang/reflect/Method")
	methodArr = methodClass.array_class().new_array(methodCount)

	stack = frame.operand_stack
	stack.push_ref(methodArr)

	#  create method objs
	if methodCount > 0:
		thread = frame.thread
		methodObjs = methodArr.refs()
		methodConstructor = methodClass.get_constructor(_methodConstructorDescriptor)
		for i, method in enumerate(methods):
			methodObj = methodClass.new_object()
			methodObj.extra = method
			methodObjs[i] = methodObj

			ops = OperandStack(11)
			ops.push_ref(methodObj)                                                #  this
			ops.push_ref(classObj)                                                 #  declaringClass
			ops.push_ref(string_pool.jstring(classLoader, method.name))                 #  name
			ops.push_ref(toClassArr(classLoader, method.parameter_types()))         #  parameterTypes
			ops.push_ref(method.ReturnType().jclass)                             #  returnType
			ops.push_ref(toClassArr(classLoader, method.exception_types()))         #  checkedExceptions
			ops.push_int(method.access_flags)                              #  modifiers
			ops.push_int(0)                                                 #  todo: slot
			ops.push_ref(getSignatureStr(classLoader, method.signature))         #  signature
			ops.push_ref(toByteArr(classLoader, method.annotationData))          #  annotations
			ops.push_ref(toByteArr(classLoader, method.parameterAnnotationData)) #  parameterAnnotations
			ops.push_ref(toByteArr(classLoader, method.annotationDefaultData))   #  annotationDefault

			shimFrame = new_shim_frame(thread, ops)
			thread.push_frame(shimFrame)

			#  init methodObj
			invoke_method(shimFrame, methodConstructor)
		
	
