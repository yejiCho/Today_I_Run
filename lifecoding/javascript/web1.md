# web

## HTML과 javascript의 만남2 (이벤트)

```html

<html>
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body>
        <!-- value button에 글씨표시 -->
        <input type="button" value="hi">
        <!-- input 내용이 변했을때 -->
        <input type="text" onchange="alert('changed')"/>
        <!-- key(키보드 버튼)를 누를때마다 표시  -->
        <input type="text" onkeydown="alert('key down!')"/>
    </body>
</html>

```

## HTML과 Javascript의 만남3 (콘솔)

```javscript

문자 갯수를 세어줌
alert('test'.length)

console에서 실행시키는 것은 해당 웹페이지를 대상으로 동작하는 것임
```

**element에서 ESC를 누르면 console창이 같이뜸 **

## 데이터타입 - 문자열과 숫자

```javascript

"hello world"
'hello world'

// str을 대문자로 표시
str.toUpperCase()
// str에서 해당하는 값의 index위치 찾기
str.indexOf('o')
// 공백제거
str.trim()
```

## 변수와 대입 연산자

```
바뀔 수 있는 어떤 값 : 변수

변수를 왜 쓰는가? (재사용성, 반복사용)

실행을 유보하고 싶을 때는 shift + enter

```

## 웹 브라우저 제어

## CSS 기초

