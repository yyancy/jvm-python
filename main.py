import pprint
import io


pp = pprint.PrettyPrinter(indent=4)
# constant pool enum
CONSTANT_CLASS               =   7
CONSTANT_FIELDREF            =   9
CONSTANT_METHODREF           =   10
CONSTANT_INTERFACE_METHODREF =   11
CONSTANT_STRING              =   8
CONSTANT_INTEGER             =   3
CONSTANT_FLOAT               =   4
CONSTANT_LONG                =   5
CONSTANT_DOUBLE              =   6
CONSTANT_NAME_AND_TYPE       =   12
CONSTANT_UTF8                =   1
CONSTANT_METHOD_HANDLE       =   15
CONSTANT_METHOD_TYPE         =   16
CONSTANT_INVOKE_DYNAMIC      =   18
def read_ubytes(f, count):
    return int.from_bytes(f.read(count),'big')

def read_bytes(f, count):
    return f.read(count)

def read_u1(f):
    return read_ubytes(f, 1)

def read_u2(f):
    return read_ubytes(f, 2)
def read_u4(f):
    return read_ubytes(f, 4)
def read_u8(f):
    return read_ubytes(f, 8)

def read_constant_pool(f, clazz):
    constant_pool = [{}]
    for i in range(1, clazz['constant_pool_count']):
        tag = read_u1(f)
        print(f"{tag=}")
        if tag == CONSTANT_METHODREF or tag == CONSTANT_FIELDREF or tag == CONSTANT_INTERFACE_METHODREF:
            info = {"tag":tag}
            info["class_index"] = read_u2(f)
            info["name_and_type_index"] = read_u2(f)
            constant_pool.append(info)
            print(info)
        elif tag == CONSTANT_STRING:
            info = {"tag":tag}
            info["string_index"] = read_u2(f)
            constant_pool.append(info)
        elif tag == CONSTANT_CLASS:
            info = {"tag":tag}
            info["name_index"] = read_u2(f)
            constant_pool.append(info)
        elif tag == CONSTANT_NAME_AND_TYPE:
            info = {"tag":tag}
            info["name_index"] = read_u2(f)
            info["descriptor_index"] = read_u2(f)
            constant_pool.append(info)
            print(info)
        elif tag == CONSTANT_UTF8:
            info = {"tag":tag}
            info["length"] = read_u2(f)
            info["value"] = read_bytes(f, info["length"]).decode("utf-8")
            constant_pool.append(info)
        else:
            raise Exception(f"to be implemented {tag}")
    return constant_pool

def at_pool(clazz,index):
    return clazz['constant_pool'][index]

def big(bs):
    return int.from_bytes(bs, 'big')

def execute_method(clazz):
    print(at_pool(clazz, clazz['methods'][0]['attributes'][0]['attribute_name_index']))
    s = io.BytesIO( clazz['methods'][0]['attributes'][0]['bytes'])
    code = {}
    code['max_stacks'] = read_u2(s)
    code['max_locals'] = read_u2(s)
    code['code_length'] = read_u4(s)
    code['bytes'] = read_bytes(s,code['code_length'])
    print(at_pool(clazz, code['max_stacks']))
    print(code['bytes'])
    pp.pprint(b'\xb7')



with open("Demo.class",'rb') as f:
    clazz = {}
    clazz['magic']= hex(int.from_bytes(f.read(4),'big'))
    clazz['minor_version']= hex(int.from_bytes(f.read(2),'big'))
    clazz['major_version'] = hex(int.from_bytes(f.read(2),'big'))
    clazz['constant_pool_count'] = int.from_bytes(f.read(2),'big')
    clazz["constant_pool"] = read_constant_pool(f, clazz)
    print(f"{clazz}")
    clazz['access_flags'] = int.from_bytes(f.read(2),'big')
    print("access_flags", format(clazz['access_flags'],"016b"))
    clazz['this_class'] = int.from_bytes(f.read(2),'big')
    print("class", clazz['constant_pool'][clazz['constant_pool'][clazz['this_class']]['name_index']])

    clazz['super_class'] = int.from_bytes(f.read(2),'big')
    print("class", clazz['constant_pool'][clazz['constant_pool'][clazz['super_class']]['name_index']])

    clazz['interfaces_count'] = read_u2(f)
    clazz['interfaces'] = []
    for i in range(0, clazz['interfaces_count']):
        clazz['interfaces'].append(int.from_bytes(f.read(2),'big'))

    clazz['fields_count'] = read_u2(f)
    clazz['fields ']= []
    for i in range(0, clazz['fields_count']):
        field = {}
        field['access_flags'] = read_u2(f)
        field['name_index'] = read_u2(f);
        field['descriptor_index'] = read_u2(f);
        field['attributes_count'] = read_u2(f);
        attributes = []
        field['attributes'] = attributes
        for j in range(0, field['attributes_count']):
            attribute = {}
            attribute['attribute_name_index'] = read_u2(f)
            attribute['attribute_length'] = read_u4(f)
            attribute['bytes'] = read_bytes(f,attribute['attribute_length'])
            attributes.append(attribute)
        clazz['fields'].append(field)

    clazz['methods_count'] = read_u2(f)
    print("method count=", clazz['methods_count'])

    clazz['methods']= []
    for i in range(0, clazz['methods_count']):
        method = {}
        method['access_flags'] = read_u2(f)
        method['name_index'] = read_u2(f);
        print("method name", clazz['constant_pool'][method['name_index']])
        method['descriptor_index'] = read_u2(f);
        method['attributes_count'] = read_u2(f);
        attributes = []
        for j in range(0, method['attributes_count']):
            attribute = {}
            attribute['attribute_name_index'] = read_u2(f)
            attribute['attribute_length'] = read_u4(f)
            attribute['bytes'] = read_bytes(f,attribute['attribute_length'])
            attributes.append(attribute)
        method['attributes'] = attributes
        clazz['methods'].append(method)

    clazz['attributes_count'] = read_u2(f);
    clazz['attributes']= []
    for j in range(0, clazz['attributes_count']):
        attribute = {}
        attribute['attribute_name_index'] = read_u2(f)
        attribute['attribute_length'] = read_u4(f)
        attribute['bytes'] = read_bytes(f,attribute['attribute_length'])
        clazz['attributes'].append(attribute)
    pp.pprint("---------------------")
    pp.pprint(clazz)
    pp.pprint(at_pool(clazz, clazz['methods'][1]['descriptor_index']))
    pp.pprint(at_pool(clazz, clazz['methods'][1]['name_index']))
    pp.pprint(at_pool(clazz, clazz['methods'][1]['attributes'][0]['attribute_name_index']))
    execute_method(clazz)



