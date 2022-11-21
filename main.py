
with open("Demo.class",'rb') as f:
    clazz = {}
    clazz['magic']= hex(int.from_bytes(f.read(4),'big'))
    clazz['minor_version']= hex(int.from_bytes(f.read(2),'big'))
    clazz['major_version'] = hex(int.from_bytes(f.read(2),'big'))
    print(f"{clazz}")

