~~~html
 DTL

	{% for menu in my_list %}
        <p>{{ menu }}</p>
    {% endfor %}
    <hr>
    {% for menu in my_list %} 
        {{ forloop.counter }}      ==> 숫자 메겨주는 것
        {% if forloop.last %}	==> last, first 두개 있는데, 첫번째 거랑 마지막 꺼 바꿔줌	
            <p>짜장면+고춧가루</p>
        {% else %}
            <p>{{ menu }}</p>
        {% endif %}
    {% endfor %}
~~~



~~~html
    {% empty %}
        <p>지금 가입한 회원이 없습니다.</p>
    {% endfor %}
==> 비면 아래꺼 출력
~~~



~~~html
    <h3>2. 조건문</h3>
    {% if '짜장면' in my_list %}
        <p>'짜장면엔 고춧가루지!!!</p>
    {% endif %}    
~~~



settings.py에서 

TEMPLATES에   'DIRS': [os.path.join(BASE_DIR, 'django_intro', 'templates')], 써야됨.

​		==> PROJECT01/django_intro/templates/ 라는 뜻 상대경로가 