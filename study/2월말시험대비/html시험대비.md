# 과목평가 web

## html(hyper text markup language)

##### head 요소

- 문서 제목, 문자코드(인코딩)와 같이 해당 문서 정보를 담고 있으며, 브라우저에 나타나지 않는다.
- CSS 선언 혹은 외부 로딩 파일 지정 등을 작성합니다.
- og와 같은 메타태그 선언이 이뤄진다.

##### body 요소

- 브라우저 화면에 나타나는 정보로 실제 내용에 해당한다.

#### 2.1. 요소(Element)

HTML의 element는 태그와 내용(contents)로 구성되어 있다.

```html
<h1>웹문서</h>
태그는 대소문자 구별 x  소문자로 작성함 
요소간의 중첩도 가능
```

#### 2.2 self-closing element

닫는 태그가 없는 태그도 존재.

```html
<img src="url"/>
```

#### 2.3 속성(Attribute)

태그에는 속성이 지정될 수 있다.

```html
<a href="google.com"/>
```

id, class, style은 태그와 상관없이 모두 사용 가능하다.



#### 시맨틱 태그

컨텐츠의 의미를 설명하는 태그로서, HTML5에 새롭게 추가된 시맨틱 태그가 있다.

의미를 가지는 태그들을 활용하기 위한 노력

| 태그    | 설명                                                         |
| ------- | ------------------------------------------------------------ |
| header  | 헤더 ( 문서 전체나 섹션의 헤더)                              |
| nav     | 내비게이션                                                   |
| aside   | 사이드에 위치한 공간으로, 메인 콘텐츠와 관련성이 적은 콘텐츠에 사용 |
| section | 문서의 일반적인 구분으로 컨텐츠의 그룹을 표현하며, 일반적으로 h1~h6 요소를 가짐 |
| article | 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역(포럼/신문 등의 글 또는 기사) |
| footer  | 푸터(문서 전체나 섹션의 푸터)                                |

~~~html
<a href="https://www.python.org/3/" target='blank'><h2 >파이썬</h2></a>
~~~

![1550899538459](C:\Users\LG\AppData\Roaming\Typora\typora-user-images\1550899538459.png)



누르면  저 주소로 새창으로 띄워줌



~~~html
 <section>
        <table>
            <tr>
                <th></th>
                <th>월</th>
                <th>화</th>
                <th>수</th>
            </tr>
            <tr>
                <td>A코스</td>
                <td colspan="2">짬뽕</td>
                <td rowspan="2">초밥</td>
            </tr>
            <tr>
                <td>B코스</td>
                <td>김치찌개</td>
                <td>삼계탕</td>
            </tr>
        </table>
    </section>

    <section>
        <table>
            <tr>
                <th>TIME</th>
                <th>INDOOR</th>
                <th colspan="2">OUTDOOR</th>
            </tr>

            <tr>
                <td></td>
                <td>소극장</td>
                <td>잔디마당</td>
                <td>대공연장</td>
            </tr>

            <tr>
                <td>10:00</td>
                <td rowspan="2">안녕하신가영</td>
                <td></td>
                <td>10CM</td>
            </tr>

            <tr>
                <td>13:00</td>
                <td rowspan="2">선우정아</td>
                <td rowspan="2">참깨와솜사탕</td>
            </tr>

            <tr>
                <td>15:00</td>
                <td></td>
            </tr>

            <tr>
                <td>17:00</td>
                <td>크러쉬</td>
                <td></td>
                <td>폴킴</td>
            </tr>
        </table><br><br>
~~~

![1550900470239](C:\Users\LG\AppData\Roaming\Typora\typora-user-images\1550900470239.png)

-----

## CSS(Cascading Style Sheet)

css 적용 우선순위
1. 속성 값 뒤에 !important 를 붙인 속성
2. HTML에서 style을 직접 지정한 속성
3. #id 로 지정한 속성
4. .클래스, :추상클래스 로 지정한 속성
5. 태그이름 으로 지정한 속성
6. 상위 객체에 의해 상속된 속성 



#### HTML은 정보와 구조화, CSS는 styling의 정의,,,    각자 문법이 다른 별개의 언어



##### 기본 사용법

```css
h1 {color:blue; font-size: 15px;}

h1 => 셀렉터
color: blue; , font-size: 15px;  => tjsdjs
color, font-size     =>  프로퍼티(property)
blue,   15ppx    => 값(value)
```

### 

### CSS 활용하기 1. Inline(인라인)

```html
<h1 style="color:blue; font-size:100px">
    This is site
</h1>
```

위와 같이 HTML 요소의 style에 CSS 넣기



#### CSS 활용하기 2. Embedding(내부 참조)

```html
<head>
    <style>
        h1 {
            color: blue;
            font-size: 100px
        }
    </style>
</head>
```

HTML 내부에 CSS를 포함시키기



### CSS 활용하기 3. link file(외부참조)

```html
<link rel='stylesheet' href='mystyle.css'>
```

외부에 있는 css파일을 로드하기



### 2. 크기단위

​	2.1 px

​	=> 디바이스별 픽셀의 크기는 제각각

​	2.2 %

​	=>요소에 지정된 사이즈(상속된 사이즈나 디폴트 사이즈)에 상대적인 사이즈를 설정한다.

​	2.3 em

​	=> em은 배수 단위로 상대 단위이다.  요소에 지정된 사이즈( 상송된 사이즈나 디폴트 사이즈)에 상대적인 사이즈를 설정한다.

​	2.4 rem

​	=> em의 기준은 상속의 영향을 바뀔 수 있다. 즉, 상황에 따라 1.2 em은 각기 다른 값을 가질 수 있다.

rem은 최상위 요소(html)의 사이즈를 기준으로 삼는다.

rem의 r은 root를 의미한다.

​	2.5 Viewport 단위

​	=> 디바이스마다 다른 크기의 화면을 가지고 있기 때문에 상대적인 단위인 viewport를 기준으로 만든 단위

| 단위 | 비고                              |
| ---- | --------------------------------- |
| vw   | 너비의 1/100                      |
| vh   | 높이의 1/100                      |
| vmin | 너비 또는 높이 중 작은 쪽의 1/100 |
| vmax | 너비 또는 높이 중 큰 쪽의 1/100   |

### 3. 색상 표현 단위

| 단위 | 비고           |
| ---- | -------------- |
| HEX  | #ffffff        |
| RGB  | rgb(0,0,0)     |
| RGBA | rgb(0,0,0,0.5) |

### box model

![1550989913065](C:\Users\LG\AppData\Roaming\Typora\typora-user-images\1550989913065.png)

### display

#### 1. block

항상 새로운 라인에서 시작한다. 화면 전체의 가로폭을 차지한다. block 레벨 요소 내에 inline 레벨 요소를 포함할 수 있다. 

block 레벨 요소 예

=> div, h1~h6, p, ol, ul, li, hr, table, form

#### 2. inline

새로운 라인에서 시작되지 않으며 문장의 중간에 들어갈 수 있음. content의 너비만큼 가로폭 차지

width, height, margin-top, margin-bottom 프로퍼티 지정 X 상하 여백은 line-height로 지정

line 레벨 요소 예

=>span, a, strong, img, br, input, select, textarea, button



#### None :  해당 요소 화면에 표시 X( 공간조차 사라짐)

#### hidden: 해당요소 안보임, 공간은 존재

```html
<PRE>
    아무거나
    어떻게쳐도
    내가
    친
    대
    로
    들어ㅏ가!!!!
</pre>
```





### Position

요소의 위치를 정의!



#### 1. static(기본위치)

기본적인 요소의 배치 순서에 따라 위에서 아래로, 왼쪽에서 오른쪽으로 순서에 따라 배치되며 부모 요소 내에 자식 요소로서 존재할 때는 보무 요소의 위치를 기준으로 배치

#### 2. relative(상대위치)

기본 위치를 기준으로 좌표 프로퍼티(top, bottom, left, right)를 사용하여 위치 이동



#### 3. absolute(절대위치)

부모 요소 또는 가장 가까이 있는 조상요소(static 제외)를 기준으로 좌표 프로퍼티(top, botom, left, right)만큼 이동한다.

즉 relative, absolute, fixed 프로퍼티가 선언되어 있는 부모 또는 조상 요소를 기준으로 위치가 결정된다.

#### 4. fixed(고정위치)

부모 요소와 관계없이 브라우저의 viewport를 기준으로 

좌표 프로퍼티(top, bottom, left, right)을 사용하여 위치를 이동시킨다. 스크롤이 되더라도 화면에서 사라지지 않고 항상 같은 곳에 위치한다.







```css
*{
    color: crimson;
}
h1 {
    color: darkblue;
}
.pink{
    color: pink;
}
#green {
    color:darkgreen;
}
```

~~~html
<p class="bold blue pink">선택자 볼드체</p>
라고 써잇고
~~~

```css
h1 {
    color: darkblue;
}
.pink{
    color: pink;
}
#green {
    color:darkgreen;
}

h2 {
    color: black;
}
.blue {
    color: blue;
}

.bold {
    font-weight: bold;
}
```

라고 css에 있을때 3개가 한번에 css에 가서 위에부터적용된다고 생각하면됨.

따라서,  blue가 pink보다 밑에 잇으니까 page에 글자 색이 파란색으로 나옴



### 형제..

```css
.red + .blue + div {
    background-color: purple;
}

/* h1의 형제 태그인 p를 바꾸는거. */
h1 + p {
    color: darkgreen;
}
```

```html
 <div class="red"></div>
    <div class="blue"></div>
    <div></div>
    <div></div>


    <hr>
    <h1>H1</h1>
    <p>h1의 형제 p</p>
    <p>넌 형제가아니지?</p>
    <hr>

```

![1550904908471](C:\Users\LG\AppData\Roaming\Typora\typora-user-images\1550904908471.png)



### 자식 선택자

```html
    <!-- 자식선택자 -->
    <ol>
        <li>ol태그의 자식 li</li>
    </ol>

    <ol id="chocolate">
        <li>허쉬</li>
        <li>드림카카오</li>
        <li>쿠앤크</li>
    </ol>
   
   
```



```css
 /* > 자식선택자 */
ol > li {
    color: crimson;
}

ol#chocolate>li {
    color: chocolate;
}

ul li {
    color: lime;
}

```

![1550905173202](C:\Users\LG\AppData\Roaming\Typora\typora-user-images\1550905173202.png)



### 자손 선택자

```css
ul li {
    color: lime;
}

/* ul 안에 li 애들 중에 두번째 애만 검정으로! */
ul li:nth-of-type(2) {
    color: black;
}

ul li:nth-child(2) {
    color: skyblue;
}

/* 형제:nth-of-type(2) 같은 타입 형제중에 2번째 */
/* 형제:nth-child(2) 자식중에 2번째 */
```

```html
    <ul>
        <div>
            <li>자식1</li>
            <li>자식2</li>
            <li>자식3</li>
        </div>
        <li>자식</li>
        <li>자식</li>
        <li>자식</li>
    </ul>
    
```

![1550908684124](C:\Users\LG\AppData\Roaming\Typora\typora-user-images\1550908684124.png)

03.css, 03_selector_2.html 다시해보아여 type child 지워가면서 해보아여





```css
.border-box {
    box-sizing: border-box;
}
==>>> 박스 사이즈를 고정한담에 다른게 적용됨
ex) 패딩 10을 주면 100짜리가 120 * 120이 되지만 저걸 사용하면 100*100 사이즈 그대로에 패딩이 10씩 들어가는 것.

/* top right bottom left   3개쓰면 top, right/left, bottom   2개면 top/bottom, left/right */
.margin-50 {
    margin: 50px;
}

.margin-top-100{
    margin-top: 100px;
}

.margin-3 {
    margin: 10px 20px 30px;
}    
    
.border {
    /* 네방향 한방에 다주기
    border: 5px black dashed; */
    border-style: dashed;
    border-bottom-style: double;
    border-top-style: solid;
    border-left-style: inset;
    border-bottom-color: aqua;
}
==>테두리모양
```

```html
    <div class="square" style="margin: auto;">
        <p>가운데 정렬</p>
    </div>
    <div class="square" style="margin-left: auto;">
        <p>오른쪽 정렬</p>
    </div>

==>박스 위치 정렬하기

    </div>
    <hr>
    <div class="circle">
    </div>

    <div class="football">
        
    </div>
동그라미랑 럭비공 만들기
```

```css
.circle {
    width: 200px;
    height: 200px;
    background-color: darkgreen;
    border-radius: 100px;
    /* 퍼센트로도 깎임 */
    /* border-radius: 50%; */
}

.football {
    width: 200px;
    height: 200px;
    background-color: crimson;
    border-radius: 10% 75%;
    opacity: 0.1;         /*투명도 설정*/
}
사각형 깎기 기억!
반지름이 100px인 원이 접하게 생긴다. %도 같고..
```

### 05. display

```html
    인라인 : <input type="text">
    <span>인라인</span>
    <a href="#">인라인</a>
```

줄 안바뀌는 친구들

```css
.none{
    display: none;
}
/* 공간도 사라지게 해 마치... 있던자리 그 위에 덮어쓰는거*/
.hidden {
    visibility: hidden;
}
```



### 07_box

relative 쓰면 큰박스에 상대적으로 relative 쓴애들끼리 위에서 아래로 차례로 줄세우기가 됨    absolute는 고냥 그 위치에 뿅하고 생김 박스에 자식들은 아무 설정 안주면 지 부모 위에 덮어서 2중으로 되어있음 ex) green의 밑에 purple 주면 purple박스만 보임      



---

## BOOTSTRAP

`CDN` : content Delivery(Distribution) Network

​	컨텐츠를 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템



### Utilities

1. spacing

   .m-0    ==>  margin : 0

   .mr-0 == > margin-right:0

   .mx-0 ==> margin-left:0      margin-right:0

   .py-0 ==> padding-top:0     padding-bottom:0

   .mt-1 ==> margin-top: 0.25 rem

   ​		margin-top: 4px



| m    | margin  |
| ---- | ------- |
| p    | padding |



| t    | top         |
| ---- | ----------- |
| l    | left        |
| r    | right       |
| x    | left, right |
| y    | top, bottom |



| 0    | 0     | 0px  |
| ---- | ----- | ---- |
| 1    | 0.25  | 4px  |
| 2    | 0.5   | 8px  |
| 3    | 1     | 16px |
| 4    | 1.5   | 24px |
| 5    | 3     | 48px |
| n1   | -0.25 | -4px |

.my-n0    => 음수도 가능

 .mx-auto 



2. color

   | primary   | 파랑  |
   | --------- | ----- |
   | secondary | 회색  |
   | success   | 초록  |
   | info      | 청록? |
   | warning   | 노랑  |
   | danger    | 빨강  |
   | light     | 하얀  |
   | dark      | 검정  |

   background-color : primary 

   ==> .bg-primary

   color: success

   ==> .text-success

   `활용` : .alert-warning

   ​	    .btn-secondary

   ​	    .navbar-dark.bg-primary

3. border

   .border

   .border-color: success

   ==> .border.border-success

   radius

   ==> .rounded-

   ==> .rounded-circle

   ==> .rounded-pill

   

   4. display

   display:block

   =>.d-block       .d-none    .d-inline    .

|              | Extra small(<576px) | Small (>=576px) | Medium(>=768) | Large(>=992) | Extra large(>=1200px) |
| ------------ | ------------------- | --------------- | ------------- | ------------ | --------------------- |
| class prefix |                     | sm              | md            | lg           | xl                    |

off-set-5    왼쪽에 5 떼고 

5. position

```css
.position-static{
    position: static !important;
}
.position-relative{
    position: relative !important;
}
.position-absolute{
    position: absolute !important;
}
.position-fixed{
    position: fixed !important;
}
.fixed-top {
    position: fixed;
    top:0;
    right:0;
    left:0;
    z-index: 1030;
}
.fixed-bottom {
    position: fixed;
    right:0;
    bottom: 0;
    left: 0;
    z-index: 1030;
}
```

6. Text

```css
.text-left {
    text-align: left
}
.text-right {
    text-align: right
} 
.text-center {
    text-align: center
}
```



![1550918131259](C:\Users\LG\AppData\Roaming\Typora\typora-user-images\1550918131259.png)



반응형 클때   (col-xl-2 : 한칸이 12중에 2차지 즉 6개 나오기 가능)6개 ->  4개 -> 3개 ->2개 ->1개 

~~~html
    <div class="container border border-dark">
        <div class="row">
            <div class="border border-dark col-xl-2 col-lg-3 col-md-4 col-sm-6 col-12 bg-warning">1번말</div>
            <div class="border border-dark col-xl-2 col-lg-3 col-md-4 col-sm-6 col-12 bg-warning">2번말</div>
            <div class="border border-dark col-xl-2 col-lg-3 col-md-4 col-sm-6 col-12 bg-warning">3번말</div>
            <div class="border border-dark col-xl-2 col-lg-3 col-md-4 col-sm-6 col-12 bg-warning">3번말</div>
            <div class="border border-dark col-xl-2 col-lg-3 col-md-4 col-sm-6 col-12 bg-warning">3번말</div>
            <div class="border border-dark col-xl-2 col-lg-3 col-md-4 col-sm-6 col-12 bg-warning">3번말</div>
        </div>
    </div>


~~~



```html
        .container {
            display: flex;
            /* display: inline-flex; */
            height: 100vh;
            border: 10px solid royalblue;
            /* flex-direction: row; */
            /* flex-direction: column; */
            /* flex-direction: row-reverse; */
            flex-direction: column-reverse;
            /* flex-wrap: wrap; */
            /* flex-wrap: nowrap; */
            
            /* css shortcul */
            /* 밑에거는 기본 디폴트값 */
            /* flex-flow: row nowrap; */

        }
```



# wrap이 멉니까!!!!



## Django

### 0. 준비사항

가상환경 생성 => 프로젝트 폴더 생성 및 이동 => local 가상환경 활성화 => django 설치

```bash
$ pyenv virtualenv 3.6.7 django-venv
 =>가상환경 생성
$ mkdir PROJECT01
$ cd PROJECT
 =>프로젝트 폴더 생성 및 이동
$ pyenv local django-venv
(django-venv) $ 
 => local 가상환경 활성화
$ pip install django
 =>django 설치
```

### 1. Django start

#### 1.1 django project

   1. 프로젝트 생성

      가상환경이 활성화 된 현재 폴더 안에 프로젝트를 생성. 명령어 뒤 `.` 주의

      project 생성할때, python이나 Django에서 사용중인 이름은 피할것

      `-`  사용 못함    (ex. django, test, class, django-test...)

      ```bash
      $ django-admin startproject django_intro .
      ```

2.  서버 실행

   ```bash
   $ python manage.py runserver $IP:$PORT
   # $ python manage.py runserver 0.0.0.0:8080
   ```

   c9에서 Invalid HTTP_HOST header error가 발생

   - `settings.py`에서 `ALLOWED_HOSTS` 와일드카드 설정

   ```python
   ALLOWED_HOSTS = ['*']
   # or 
   ALLOWED_HOSTS = ['example-username.c9users.io']
   # https://,  :8080을 제외한 URL
   ```

3. git ignore 설정

   ```bash
   $ touch .gitignore
   #c9에선 c9 open .gitignore
   ```

   .gitignore 파일에 gitignore 사이트에서 받은 django 관련 복붙

4. TIME_ZONE, LANGUAGE_CODE 설정

   - `settings.py`

     ```python
     LANGUAGE_CODE = 'ko-kr'
     TIME_ZONE = 'Asia/Seoul'
     ```

5.  서버 재실행 및 한글화 확인 (로켓)

6.  프로젝트 구조

   ```bash
   PROJECT01/
       manage.py
       django_intro/
           __init__.py
           settings.py
           urls.py
           wsgi.py
   	db.sqlite3
   ```

- `PROJECT01/`: 디렉토리 바깥의 디렉토리는 단순히 프로젝트를 담는 공간. 이 이름은 Django와 상관 없음, 원하는 이름으로 변경가능
- `manage.py`: Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인의 유틸리티.
- `django_intro/` : 디렉토리 내부에는 project를 위한 실제 python 패키지들이 저장됨. 이 디렉토리 내의 이름을 이용하여, (`django_intro.urls`와 같은 식으로) project 어디서나 python 패키지들을 import 할 수 있다.
- `__init__.py` : Python으로 하여금 이 디렉토리를 패키지 처럼 다루라고 알려주는 용도의 단순한 빈 파일.
- `settings.py` : 현재 Django project의 모든 환경/ 구성을 저장.
- `urls.py` : 현재 Django project의 URL 선언을 저장. Django로 작성된 사이트의 "목차". 사이트의 url과 views의 연결을 지정. 모든 url 매핑 코드가 포함될 수 있지만, 특정한 어플리케이션에 매핑의 일부를 할당해 주는 것이 일반적.
- `wsgi.py` : 현재 project를 서비스 하기 위한 WSGI 호환 웹서버의 진입점.
  - `WSGI(Web server gateway interface)`:파이썬 웹 프레임워크에서 사용하는 웹서버 규칙

#### 1.2 django application

- 실제로 특정한 역할을 해주는 친구가 바로 application
- 프로젝트는 이러한 어플리케이션의 집함, 실제 요청을 처리하고 페이지를 보여주고 하는 것들은 이 어플리케이션의 역할
- 하나의 프로젝트는 여러 개의 어플리케이션을 가질 수 있다.
  - 어플리케이션은 하나의 역할 및 기능 단위로 쪼개는 것이 일반적, 작은 규모의 서비스에서는 잘 나누지 않음.  나누는 것에 대한 기준도 딱히 없음
- 각각의 어플리케이션은 MTV 패턴으로 구성되어 있다.

1. Application 만들기

   ```bash
   $ python manage.py startapp home
   ```

2. Application 구조

   ```bash
   home/
   	__init__.py
   	admin.py
   	apps.py
   	models.py
   	tests.py
   	views.py
   	migrations/
   		__init__.py
   ```

   - `admin.py`: 관리자용 페이지 커스터마이징 장소.
   - `apps.py`: 앱의 정보가 있는 곳. 우선 우리는 수정할 일이 없음.
   - `models.py` : 앱에서 사용하는 Model을 정의하는 곳.
   - `test.py`: 테스트 코드를 작성하는 곳.
   - `views.py` : view들이 정의 되는 곳. 사용자에게 어떤 데이터를 보여줄지 구현하는 곳.

3. Application 등록

   - 방금 생성한 application을 사용하려면 프로젝트에게 앱을 만들었다고 알려주어야 사용 가능하다.
   - `home > apps.py > class HomeConfig()` 구조 이기 때문에 `home.apps.HomeConfig` 로 작성한다.

   - `settings.py` 

   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'home.apps.HomeConfig',
   ]
   
   ```

---

### 2. MTV

- 장고를 제외하면 일반적으로 MVC
  - Model: 어플리케이션의 핵심 로직의 동작을 수행한다.(Database)
  - Template(View): 어떻게 데이터가 보여질지를 수행한다.(Interface)
  - View(Controller): 어떤 데이터를 보여줄지를 구현한다.(Logic)
- .py 3대장
- `models.py`: 데이터베이스 관리
- `views.py` : 페이지 관리(페이지 하나 당, 하나의 함수)
- `urls.py` : 주소(URL) 관리

---

### 3. views-urls

1. views.py
2. urls.py
3. templates   순으로 작성









---

inline block,

시맨틱 태그 이름장난  6개 종류

=> footer, aside, nav, article, section, header

img  => src인데 href 넣고 

a태그엔 href

form에 action

input에 name    value

css로 링크하는거 

열닫 일체 태그

nth child, nth type

rem은 html속성 기준 기본 pixel에 *  기본속성은 16px

em은 바로 위 부모  부모가 없으면 body  























