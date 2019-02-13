# Django

MVC  ==>>>> MTV 장고는 왜 MTV인가 

뷰                      템플릿



zzu.li/djpy2_c9 에서 두덩어리  c9 bash창에 설치하고 

pyenv virtualenv 3.6.7 django-venv   가상환경 

pyenv virtualenvs로 가상환경 됐나 확인

pyenv local django-venv 장고 가상환경 켜기

django-admin startproject first_workshop .       프로젝트만들기 ex)PROJECT01 같이 큰거

python manage.py startapp student      애들 생김 앱 생성

INSTALLED_APPS에 'student.apps.StudentConfig',  앱 등록

python manage.py runserver $IP:$PORT    서버 키는 명령어.



#### settings.py 

ALLOWED_HOSTS = [주소]   주소자리에 * 치면 모든거 열기

ex) ['django-intro-sochic2.c9users.io']

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'





- 앱마다 MTV구조를 갖추고 있다..



- 사용자들에게 보여지는 곳이 (views.py) MTV 중 View다.



- django_intro에 settings.py에  INSTALLED_APPS에 'home.apps.HomeConfig' 써서 등록

  ​	home이라는 app을 만들었다는 것을 등록하는 느낌



  commit 01_django settings

  ------------------

  ### 1. 처리할 views(controller)

  ### 2. 요청 urls

  ### 3. 결과 보여줄 templates

  ### 위의 순으로 앞으로 장고에서 만들 것이다!





POST로 받아올 때는 보안, 데이터베이스에 저장되는 값이니까 아무거나 못들어가게 토큰값이 수시로 바뀌면서 되게    {% csrf_token %} 쳐야 POST방식으로 받아오고 사용하고 가능.



