# iterable

```
iterable과 iterator의 차이에 대해서 알아보자!
```

## iterable

```
iterable의 의미는 member를 하나씩 차례로 반환가능한 object를 말한다.

iterable의 예로는 sequence type인 list, str, tuple이 대표적
```

```python
for x in range(5):
    print(x)

0
1
2
3
4
```

```
또한 __iter()__ 나 __getitem()__ 메소드로 정의된 class는
모두 iterable하다고 할 수있다.
```

## iterator

```
iterator는 next()메소드로 데이터를 순차적으로 호출 가능한 object이다.
만약 next()로 다음 데이터를 불러 올 수 없을 경우(가장 마지막 데이터인 경우) Stopliteration exception을 발생
```

```
iterable한 object들은 iterator인가?
--> iterable한다고 반드시 iterator라는 것은 아니다.
```

```python
>>> x = [1,2,3]

>>> next(x)

Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

TypeError: list object is not an iterator
```

```
list 는 iterable 이지만, 위와 같이 next() 메소드로 호출해도 동작하지 않는다. iterator 가 아니라는 에러 메시지를 볼 수 있다.

만약, iterable 을 iterator 로 변환하고 싶다면, iter() 라는 built-in function 을 사용하면 된다. 
```
```python
>>> x = [1,2,3]

>>> type(x)

<type 'list'>

>>> y = iter(x)

>>> type(y)

<type 'listiterator'>
```
```
위와 같이 iter()함수를 사용하여 list를 listiterator타입으로 변경 가능
```
```python
>>> next(y)

1

>>> next(y)

2

>>> next(y)

3

>>> next(y)

Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

StopIteration

```