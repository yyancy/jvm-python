from jvm.native.java.io.FileOutputStream import write_bytes
from jvm.native.java.lang.Class_getDeclaredConstructors0 import getDeclaredConstructors0
from jvm.native.java.lang.Class_getDeclaredMethods0 import getDeclaredMethods0
from jvm.native.java.lang.Double import double_to_raw_long_bits, long_bits_to_double
from jvm.native.java.lang.Float import float_to_raw_int_bits, int_bits_to_float
from jvm.native.java.lang.String import intern
from jvm.native.java.lang.System import array_copy, init_properties, set_out0
from jvm.native.java.lang.Thread import currentThread, isAlive, setPriority0, start0
from jvm.native.java.lang.Throwable import fill_in_stack_trace
from jvm.native.java.security.AccessController import doPrivileged, getStackAccessControlContext
from jvm.native.sun.Unsafe import *
from jvm.native.sun.misc.Unsafe import compareAndSwapInt, compareAndSwapLong, compareAndSwapObject, getInt, getObject
from jvm.native.sun.misc.VM import initialize, set_err0, set_in0
from jvm.native.sun.reflect.NativeConstructorAccessorImpl import newInstance0
from jvm.native.sun.reflect.Reflection import getCallerClass, getClassAccessFlags
from . import registry
import jvm.native.java.lang.Object as Object
import jvm.native.java.lang.Class as Class

registry.register('java/lang/Object', 'getClass',
                  '()Ljava/lang/Class;', Object.get_class)

jlClass = "java/lang/Class"
# Class
registry.register('java/lang/Class', 'getPrimitiveClass',
                  '(Ljava/lang/String;)Ljava/lang/Class;', Class.get_primitive_class)
registry.register('java/lang/Class', 'getName0',
                  '()Ljava/lang/String;', Class.getName0)
registry.register('java/lang/Class', 'desiredAssertionStatus0',
                  '(Ljava/lang/Class;)Z', Class.desired_assertion_status0)
registry.register("java/lang/System", "arraycopy",
                  "(Ljava/lang/Object;ILjava/lang/Object;II)V", array_copy)

registry.register(jlClass, "forName0", "(Ljava/lang/String;ZLjava/lang/ClassLoader;Ljava/lang/Class;)Ljava/lang/Class;", Class.forName0)
registry.register(jlClass, "getDeclaredFields0", "(Z)[Ljava/lang/reflect/Field;", Class.getDeclaredFields0)
registry.register(jlClass, "isInterface", "()Z", Class.isInterface)
registry.register(jlClass, "isPrimitive", "()Z", Class.isPrimitive)
registry.register(jlClass, "isAssignableFrom", "(Ljava/lang/Class;)Z", Class.isAssignableFrom)
registry.register(jlClass, "getDeclaredConstructors0", "(Z)[Ljava/lang/reflect/Constructor;", getDeclaredConstructors0)
registry.register(jlClass, "getModifiers", "()I", Class.getModifiers)
registry.register(jlClass, "getSuperclass", "()Ljava/lang/Class;", Class.getSuperclass)
registry.register(jlClass, "getInterfaces0", "()[Ljava/lang/Class;", Class.getInterfaces0)
registry.register(jlClass, "isArray", "()Z", Class.isArray)
registry.register(jlClass, "getDeclaredMethods0", "(Z)[Ljava/lang/reflect/Method;", getDeclaredMethods0)
registry.register(jlClass, "getComponentType", "()Ljava/lang/Class;", Class.getComponentType)
registry.register(jlClass, "isAssignableFrom", "(Ljava/lang/Class;)Z", Class.isAssignableFrom)


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
registry.register("java/lang/Object", "clone",
                  "()Ljava/lang/Object;", Object.clone)
registry.register("sun/misc/VM", "initialize", "()V", initialize)
registry.register("java/lang/Throwable", "fillInStackTrace",
                  "(I)Ljava/lang/Throwable;", fill_in_stack_trace)

registry.register("java/lang/System", "setIn0",
                  "(Ljava/io/InputStream;)V", set_in0)
registry.register("java/lang/System", "setOut0",
                  "(Ljava/io/PrintStream;)V", set_out0)
registry.register("java/lang/System", "setErr0",
                  "(Ljava/io/PrintStream;)V", set_err0)
registry.register("java/lang/System", "initProperties",
                  "(Ljava/util/Properties;)Ljava/util/Properties;", init_properties)
registry.register("java/io/FileOutputStream",
                  "writeBytes", "([BIIZ)V", write_bytes)


miscUnsafe = "sun/misc/Unsafe"
# Unsafe
# registry.register(miscUnsafe, "arrayBaseOffset", "(Ljava/lang/Class;)I", array_base_offset)
# registry.register(miscUnsafe, "arrayIndexScale", "(Ljava/lang/Class;)I", arrayIndexScale)
# registry.register(miscUnsafe, "addressSize", "()I", addressSize)
# registry.register(miscUnsafe, "objectFieldOffset", "(Ljava/lang/reflect/Field;)J", objectFieldOffset)

registry.register(miscUnsafe, "arrayBaseOffset", "(Ljava/lang/Class;)I", array_base_offset)
registry.register(miscUnsafe, "arrayIndexScale", "(Ljava/lang/Class;)I", arrayIndexScale)
registry.register(miscUnsafe, "addressSize", "()I", addressSize)
registry.register(miscUnsafe, "objectFieldOffset", "(Ljava/lang/reflect/Field;)J", objectFieldOffset)
registry.register(miscUnsafe, "compareAndSwapObject", "(Ljava/lang/Object;JLjava/lang/Object;Ljava/lang/Object;)Z", compareAndSwapObject)
registry.register(miscUnsafe, "getIntVolatile", "(Ljava/lang/Object;J)I", getInt)
registry.register(miscUnsafe, "compareAndSwapInt", "(Ljava/lang/Object;JII)Z", compareAndSwapInt)
registry.register(miscUnsafe, "getObjectVolatile", "(Ljava/lang/Object;J)Ljava/lang/Object;", getObject)
registry.register(miscUnsafe, "compareAndSwapLong", "(Ljava/lang/Object;JJJ)Z", compareAndSwapLong)

# Reflection
registry.register("sun/reflect/Reflection", "getCallerClass", "()Ljava/lang/Class;", getCallerClass)
registry.register("sun/reflect/Reflection", "getClassAccessFlags", "(Ljava/lang/Class;)I", getClassAccessFlags)

# AccessController
registry.register("java/security/AccessController", "doPrivileged", "(Ljava/security/PrivilegedAction;)Ljava/lang/Object;", doPrivileged)
registry.register("java/security/AccessController", "getStackAccessControlContext", "()Ljava/security/AccessControlContext;", getStackAccessControlContext)
registry.register("java/security/AccessController", "doPrivileged", "(Ljava/security/PrivilegedExceptionAction;)Ljava/lang/Object;", doPrivileged)
                  

# Thread

registry.register("java/lang/Thread", "currentThread", "()Ljava/lang/Thread;", currentThread)
registry.register("java/lang/Thread", "setPriority0", "(I)V", setPriority0)
registry.register("java/lang/Thread", "isAlive", "()Z", isAlive)
registry.register("java/lang/Thread", "start0", "()V", start0)
                  

registry.register("sun/reflect/NativeConstructorAccessorImpl", "newInstance0", "(Ljava/lang/reflect/Constructor;[Ljava/lang/Object;)Ljava/lang/Object;", newInstance0)
