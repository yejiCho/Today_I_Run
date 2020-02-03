# python pickle module

## pickle module

- 일반 텍스트를 파일로 저장할 때는 파일 입출력을 이용한다.
- 하지만 리스트나 클래스같은 텍스트가 아닌 자료형은 일반적인 파일 입출력 방법으로는 데이터를 저장하거나 불러올 수 없다.
- 파이썬에서는 이와 같은 테스트 이외의 자료형을 파일로 저장하기 위하여 pickle이라는 모듈제공

## use pickle module data input and load

- import pickle
- 원하는 데이터를 자료형의 변경없이 파일로 저장하여 그대로 로드
- open('text.txt','w')방식으로 데이터를 입력하면 string자료형으로 저장
- pickle로 데이터를 저장하거나 불러올때는 파일을 바이트형식으로 읽거나써야함
- (wb, rb)
- wb로 데이터 입력하는 경우에는 .bin확장자 사용추천

### 입력

```python
# pickle.dump(dta,file)
import pickle
list = ['a','b','c']
with open('list.txt','wb') as f:
    pickle.dump(list,f)

```

### 로드

```python
# 변수 = pickle.load(file)
while open('list.txt','rb') as f:
    data = pickle.load(f)

# pickle.load()를 사용하여 파일 전체 내용 로드
with open('abc.bin','rb') as file:
    data_list = []
    while True:
        try:
            data = pickle.load(file)
        except EOFError:
            break
        data_list.append(data)

# 한 줄씩 파일을 읽으며 더이상 로드할 데이터가 없으면 EOFError이 발생
# pickle.load(file)을 통하여 파일의 내용을 읽어오려면,pickle.dump를 사용한 파일이여야함
```

### 추가

