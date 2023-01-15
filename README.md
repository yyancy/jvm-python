# JVM in python


## Find Object class
in windows
`python .\main.py -jre "C:\Program Files\Java\jdk1.8.0_351\jre" java.lang.Object`


## Chapter 5 test
### On Linux
`python3 main.py -jre /usr/lib/jvm/java-8-openjdk-amd64/jre  data/GaussTest`
### Expected result
```bash
<LocalVars 0x7efd546146d0
  .slots = [
    None,
    <Slot 0x7efd54614940
      .num = 5050
    >,
    <Slot 0x7efd54614b80
      .num = 101
    >
  ]
>
<OperandStack 0x7efd546148b0
  .size = 0,
  .slots = [
    <Slot 0x7efd54614790
      .num = 101
    >,
    <Slot 0x7efd54614a90
      .num = 100
    >
  ]
>
2023-01-01:07:35:16,358 ERROR    [interperter.py:29] Unsupported opcode: b2

```