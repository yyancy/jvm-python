from . import registry
import jvm.native.java.lang.Object as Object
import jvm.native.java.lang.Class as Class

registry.register('java/lang/Object', 'getClass',
                  '()Ljava/lang/Class;', Object.get_class)
registry.register('java/lang/Class', 'getPrimitiveClass',
                  '(Ljava/lang/String;)Ljava/lang/Class;', Class.get_primitive_class)
registry.register('java/lang/Class', 'getName0',
                  '()Ljava/lang/String;', Class.getName0)
registry.register('java/lang/Class', 'desiredAssertionStatus0',
                  '(Ljava/lang/Class;)Z', Class.desired_assertion_status0)
