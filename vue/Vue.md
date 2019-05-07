# 디렉티브

- vue 에서 제공하는 특수 속성임을 나타내는 v- 접두어가 붙어있으며, 렌더링된 DOM에 특수한 반응형 동작을 한다.
- v-for / v-if / v-html/ v-once
- v-on : click  (add-on-eventlistener?) 인가랑 같은 일,,    디렉티브 바로 뒤에 붙는 친구들을 전달인자라고 한다.

----

## v-bind

- html 태그의 속성 값에 vue에서 만든 데이터값으로 사용해야 할 때 사용한다.

-------

## v-model

- input / select / textarea
- form 에 관련된 태그에만 사용 될 수 있다.

-----

## v-on

v-on:이벤트 이름 = "메소드이름"





## 1. 조건부 렌더링

### 	v-if

- 렌더링 할지 말지 자체를 결정

  #### v-show

- 렌더링은 항상 되고 css를 통해 보여질지 숨겨질지를 결정함



## 2. 리스트 렌더링

#### 	v-for

- 동일한 노드에 for 와 if 가 있다면 우선순위는 for가 높다. 즉 if는 for가 반복될 때마다 실행된다.

## 3. 이벤트리스너

- v-on / @
- v-on:전달인자.수식어
- ex) v-on:keyup.enter 

## 4. 데이터 바인딩

- v-bind / 생략

- v-model

## 5. 텐더링 & 컴파일 관련

- v-pre  : 컴파일하지 않음 ( 그대로 출력해라!)

- v-once : 처음에 단 한번만 렌더링 함
- v-cloak : 컴파일이 완료되면 사라지는 디렉티브



## 6. template element 

- `<template></template>template>`
- 보이지 않은 wrapper 역할을 한다.



# v-bind: => :	콜론은남기기

# v-on: => @		콜론까지지우기

중요중요





# METHOD(매번 계산) VS COMPUTED (CASHING)



# computed

- 미리 계산된 값을 반환

- 템플릿 내에 직접 로직을 넣을 수도 있지만, 그러면 템플릿이 너무 복잡해지기 때문에 vue 안에 정의해 두는것.   ex) {{  newTodo.split('').reverse }}   => {{  reversedNewTodo  }} 같이 간단하게 쓰게
- 이러한 로직 처리를 computed 안에 정의

