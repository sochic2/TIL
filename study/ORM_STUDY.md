## SQL

### ALTER TABLE

~~~sql
Rename TABLE
Add new column to TABLE

ALTER TABLE friends ADD COLUMN married INTEGER;
RENAME TO new_table_name;
~~~

2가지 기능



## ORM 

CRUD => READ CREATE UPDATE DELETE

Object - Relational Mapping

익숙한 자기 언어를 쓸수 있게 해줌



#### 장점

1. 객체지향적인 코드로 인해 직관적이고 비즈니스로직에 더 집중할 수 있게 한다.
2.  재사용 / 유지보수가 증가
3.  DB에 대한 종속성이 줄어듬

#### 단점 

1. 오로지 ORM으로만은 거대한 서비스를 구현하기가 어렵다.
2. 어느정도의 속도 저하가 있다. (단계가 하나 더 있어서... 번역기 역할을 하는 ORM을 거쳐가는 것이니까)
3. 장점>>>단점이라서 씀   거의 ORM을 무조건 쓰는 느낌



##### 초기설정..

flask에서... 설치해야됨 배쉬창에서

~~~bash
pip install flask_sqlalchemy
pip install flask_migrate
~~~



nullable=False    =>> 비어있을수 없다..라는 말



app.py, models.py 작성하고나서  bash창에서..

~~~bash

flask db init

flask db migrate

flask db upgrade
~~~



#### CREATE

~~~python
user = User(username='junho', email='example@gmail.com')
~~~

~~~sql
INSERT INTO user(username, email)

VALUES('junho', 'example@gmail.com')
~~~



### READ

~~~python
users=User.query.all()
~~~

~~~sql
SELECT * FROM users;
~~~



~~~python
users = User.query.filter_by(username='namki').all
~~~

~~~sql
SELECT * FROM users WHERE username='namki';
~~~



~~~python
users = User.query.filter_by(username='namki').first()
~~~

~~~sql
SELECT * FROM users WHERE username='namki' LIMIT 1;
~~~



PK만 GET으로 가져올 수 있음

~~~python
user = User.query.get(1)
~~~

~~~sql
SELECT * FROM users WHERE id=1;
~~~



LIKE

~~~python
users = User.query.filter(User.email.like('%exam%')).all()
~~~



~~~sql
users = User.query.limit(1).offset(2).all()
~~~

UPDATE  기존 있던 user.username = 'namki'에서 ssafy로 바꾸기

~~~python
user = User.query.get(1)
user.username = 'ssafy'
db.session.commit()
user.username
~~~

DELETE

~~~python
user = User.query.get(1)
db.session.delete(user)
db.session.commit()
~~~



~~~python
#app.py에서...이렇게 해서 맨 밑에 db.session.ad(user), commit 써서 ~~함

@app.route('/')
# 뷰함수, route 아래 있는 함수
def index():
    users = User.query.all()
    # url_for('index') =>>>'/'
    return render_template('index.html')
    
@app.route('/users/create')
def create():
    username = request.args.get('username')
    email = request.args.get('email')
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))
    
~~~



