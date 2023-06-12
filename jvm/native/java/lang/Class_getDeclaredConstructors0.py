
#
# Constructor(Class<T> declaringClass,
#             Class<?>[] parameterTypes,
#             Class<?>[] checkedExceptions,
#             int modifiers,
#             int slot,
#             String signature,
#             byte[] annotations,
#             byte[] parameterAnnotations)

# */
from jvm.instructions.base.method_invoke_logic import invoke_method
from jvm.native.java.lang.Class_helper import getSignatureStr, toByteArr, toClassArr
from jvm.rtda.frame import Frame, new_shim_frame
from jvm.rtda.operand_stack import OperandStack


_constructorConstructorDescriptor = (
	"(Ljava/lang/Class;" 
	"[Ljava/lang/Class;"
	"[Ljava/lang/Class;"
	"II" 
	"Ljava/lang/String;" 
	"[B[B)V"
)

#  (Z)[Ljava/lang/reflect/Constructor;
def getDeclaredConstructors0(frame :Frame):
	_vars = frame.local_vars
	classObj = _vars.get_this()
	publicOnly = _vars.get_bool(1)

	clazz = classObj.extra
	constructors = clazz.get_constructors(publicOnly)
	constructorCount = int(len(constructors))

	classLoader = frame.method.clazz.loader
	constructorClass = classLoader.load_class("java/lang/reflect/Constructor")
	constructorArr = constructorClass.array_class().new_array(constructorCount)

	stack = frame.operand_stack
	stack.push_ref(constructorArr)

	if constructorCount > 0:
		thread = frame.thread
		constructorObjs = constructorArr.refs()
		constructorInitMethod = constructorClass.get_constructor(_constructorConstructorDescriptor)
		for i, constructor in enumerate(constructors):
			constructorObj = constructorClass.new_object()
			constructorObj.extra = constructor
			constructorObjs[i] = constructorObj

			ops = OperandStack(9)
			ops.push_ref(constructorObj)                                                #  this
			ops.push_ref(classObj)                                                      #  declaringClass
			ops.push_ref(toClassArr(classLoader, constructor.parameter_types()))         #  parameterTypes
			ops.push_ref(toClassArr(classLoader, constructor.exception_types()))         #  checkedExceptions
			ops.push_int(constructor.access_flags)                              #  modifiers
			ops.push_int(0)                                                      #  todo slot
			ops.push_ref(getSignatureStr(classLoader, constructor.signature))         #  signature
			ops.push_ref(toByteArr(classLoader, constructor.annotationData))          #  annotations
			ops.push_ref(toByteArr(classLoader, constructor.parameterAnnotationData)) #  parameterAnnotations

			shimFrame = new_shim_frame(thread, ops)
			thread.push_frame(shimFrame)

			#  init constructorObj
			invoke_method(shimFrame, constructorInitMethod)
		
	

