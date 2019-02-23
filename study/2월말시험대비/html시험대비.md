# 과목평가 web

## html

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

## CSS

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

​	컨텐츠를 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공	하는 시스템



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

|              | Extra small | Small | Medium | Large | Extra large |
| ------------ | ----------- | ----- | ------ | ----- | ----------- |
| class prefix |             | sm    | mx     | lg    | xl          |

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































