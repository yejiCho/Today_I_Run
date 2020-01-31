# 🐍Python is intepretor language

```

Python은 인터프리터 언어라고 하는데, 인터프리터에 대해 간략히 알아보자.

소스코드를 기계를 컴파일해서 실행파일을 만들고 실행하는 컴파일 언어와는 다르게 인터프리터 언어는 코드를 한 줄씩 읽어 내려가며 실행하는 프로그래밍 언어이다.

인터프리터 방식을 쓰는 프로그래밍 언어의 대표적인 것은 Python이다!


```
#  🏃‍♂️How to run program?

```
Python의 구현체 CPython

일반적으로 python이 C로 구현되어 있다고 알려져 있는데 그 구현체가 CPython이다. 가장 처음 만들어진 python의 구현체이고 python.org에서 다운받으면 CPython을 받는것이다.

CPython은 인터프리터 이면서 컴파일러이다. 우리가 작성하는 Python코드를 bytecode로 컴파일하고 실행한다.
다시말해, python코드를 C언어로 바꾸는 것이 아니라 컴파일 하여 bytecode로 바꾸고 그 다음에 interpreter(virtual machine)가 실행한다.

.py 파일을 실행하면 .pyc 라는 파일이 생성되는데 이것이 CPython이 컴파일한 bytecode가 들어있는 것이다. 그 다음 .pyc를 interpret 하는 것도 CPyton이다.

```
![i_think_structer](https://i.imgur.com/c0PRvvI.png)

![structer](https://i.imgur.com/PJME67T.png)

# When create .pyc file?

```

pyc 파일은 어떠한 파일을 임포트(import)했을때 생성된다. 예를 들어 a.py안에 b.py을 import하게 되면 b.pyc파일이 생성된다.

```

#  🙄what is .pyc?

```
파이썬 가상머신(virtual machine)은 컴파일러와 인터프리터가 있다.
인터프리터는 .py파일에 작성된 원시 파이썬 코드를 곧바로 해석할 수 없다..

그렇기 때문에 우선 원시코드는 byte코드로 변환되어야 한다.
이 과정에서 .pyc파일이 생성되고 그 안에 byte코드가 작성된다.

.pyc 파일이 이미 생성되어 있으면 다시 컴파일 할 필요없이 바로 시스템에 byte코드를 적재한다.

.pyc 파일은 캐시처럼 취급된다. 미리 byte코드를 만들어 놓고 인터프리터로 코드를 실행하기 때문에 속도가 향상된다.

.py파일을 bytecode로 컴파일한 코드이기 때문에 원본 .py파일이 없어도
실행가능

```

# How to check convert bytecode?

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


# 📚References

### [How Python works?](https://velog.io/@doondoony/How-Python-works)
### [python에 대하여, python은 어떻게 동작하는가?](https://cjh5414.github.io/about-python-and-how-python-works/)
### [How Python runs?](https://indianpythonista.wordpress.com/2018/01/04/how-python-runs/)
### [Python is compiled language or interpreted language?](http://www.techdarting.com/2014/04/python-compiled-or-interpreted-language.html)
