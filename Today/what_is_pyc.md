# python에서 pyc파일은 무엇인가

```
- pyc 파일은 왜 생성될까?

pyc 파일은 어떠한 파일을 임포트(import)했을때 생성된다. 예를 들어 a.py안에 b.py을 import하게 되면 b.pyc파일이 생성된다.

- pyc 파일은 무엇인가?

파이썬 인터프리터가 파이썬 소스코드를 컴파일하여 생성하는 파일
py파일을 bytecode로 컴파일한 코드이기 때문에 원본 py파일이 없어도 실행가능.

pyc 디 컴파일

1. Uncompyle6 설치
pip install uncompyle6

2. 디컴파일
uncompyle6 <파일명.pyc>


```

# python 에서 bytecode?

```
Python의 구현체 CPython

일반적으로 python이 C로 구현되어 있다고알려져 있는데, 그 구현체가 CPython이다. 가장 처음 만들어진 python의 구현체이고 python.org에서 다운받으면 CPython을 받는 것 이다.

CPython은 인터프리터이면서 컴파일러이다. 우리가 작성하는 Python 코드를 bytecode로 컴파일하고 실행한다. 다시 말해, python코드를 C언어로 바꾸는 것이 아니라 컴파일하여 bytecode로 바꾸고 그 다음에 interpreter(virtual machine)가 실행한다.

```

```python

# dis라는 패키지를 이용하면 python코드가 어떻게 bytecode로 변환되는지 볼 수 있다.

# dis 모듈은 클래스, 메소드, 함수 및 코드 객체를 디스 어셈블하여 사람이 읽을 수 있는 Python 바이트 코드를 만들 수 있습니다.

import dis

def hello():
    print("Hello")

dis.dis(hello)

2   0   LOAD_GLOBAL   0   (print)
    2   LOAD_CONST    1   ('Hello')
    4   CALL_FUNCTION 1
    6   POP_TOP
    8   LOAD_CONST    0   (None)
    10  RETURN_VALUE

```

## 그 외의 구현체

```
Jypthon

python코드를 java 바이트코드로 만들어 JVM에서 실행할 수 있도록 한다. '.py 파일을 .class 파일로 컴파일 한다.'

PyPy

Python 자체로 구현.JIT 컴파일 도입하여 CPython보다 빠르다.

JIT(just-in-time)컴파일 이란 프로그램을 실행하기 전에 컴파일 하는 대신, 프로그램을 실행하는 시점에서 필요한 부분을 즉석으로 컴파일 하는 방식. 보통 인터프리터 언어의 성능 향상을 목적으로 도입하는 경우가 많다. 인터프리터 하면서 자주 쓰이는 코드를 캐싱하기 때문에 인터프리터의 느린 실행 속도를 개선 할 수 있다. JVM에서도 바이트코드를 기계어로 번역할 때 JIT컴파일러를 사용



IronPython(.NET Framework), Brython(JavaScript)


```

# Pypi란 무엇인가?

```


```