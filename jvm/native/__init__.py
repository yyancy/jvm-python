from jvm.native.java.lang.Double import double_to_raw_long_bits, long_bits_to_double
from jvm.native.java.lang.Float import float_to_raw_int_bits, int_bits_to_float
from jvm.native.java.lang.String import intern
from jvm.native.java.lang.System import array_copy
from jvm.native.sun.misc.VM import initialize
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
registry.register("java/lang/System", "arraycopy",
                  "(Ljava/lang/Object;ILjava/lang/Object;II)V", array_copy)

registry.register("java/lang/Float", "floatToRawIntBits",
                  "(F)I", float_to_raw_int_bits)
registry.register("java/lang/Float", "intBitsToFloat",
                  "(I)F", int_bits_to_float)
registry.register("java/lang/Double", "doubleToRawLongBits",
                  "(D)J", double_to_raw_long_bits)
registry.register("java/lang/Double", "longBitsToDouble",
                  "(J)D", long_bits_to_double)
registry.register("java/lang/String", "intern", "()Ljava/lang/String;", intern)
registry.register("java/lang/Object", "hashCode", "()I", Object.hashcode)
registry.register("java/lang/Object", "clone", "()Ljava/lang/Object;", Object.clone)
registry.register("sun/misc/VM", "initialize", "();",initialize)

