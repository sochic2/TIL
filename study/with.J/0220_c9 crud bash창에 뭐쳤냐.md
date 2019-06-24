~~~bash
(django-venv) sochic2:~/workspace/PROJECT02 $ python manage.py shell_plus
# Shell Plus Model Imports
from boards.models import Board
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
# Shell Plus Django Imports
from django.core.cache import cache
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When, Exists, OuterRef, Subquery
from django.utils import timezone
from django.urls import reverse
Python 3.6.7 (default, Feb 13 2019, 00:36:25) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> board = Board(title='second', content='django!!')
>>> board.save()
>>> Board.objects.all()
<QuerySet [<Board: 1: first>, <Board: 2: second>]>
>>> Board.objects.create(title='third', content='django!!!')
<Board: 3: third>
>>> Board.objects.all()
<QuerySet [<Board: 1: first>, <Board: 2: second>, <Board: 3: third>]>
>>> board = Board()
>>> board.title = 'fourth'
>>> board.content = 'django!!!!'
>>> board.id
>>> board.created_at
>>> board.save()
>>> board.id
4
>>> board.created_at
datetime.datetime(2019, 2, 20, 10, 35, 22, 943987)
>>> board.created_at
datetime.datetime(2019, 2, 20, 10, 35, 22, 943987)
>>> board.created_at
datetime.datetime(2019, 2, 20, 10, 35, 22, 943987)
>>> board = Board()
>>> board.title = 'asdfqweasdqweasd'
>>> board.full_clean()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/ubuntu/.pyenv/versions/django-venv/lib/python3.6/site-packages/django/db/models/base.py", line 1152, in full_clean
    raise ValidationError(errors)
django.core.exceptions.ValidationError: {'title': ['이 값이 최대 10 개의 글자인지 확인하세요(입력값 16 자).'], 'content': ['이 필드는 빈  칸으로 둘 수 없습니다.']}
>>> Board.objects.all()
<QuerySet [<Board: 1: first>, <Board: 2: second>, <Board: 3: third>, <Board: 4: fourth>]>
>>> Board.objects.filter(title='first').all()
<QuerySet [<Board: 1: first>]>
>>> Board.objects.filter(title='first').first()
<Board: 1: first>
>>> Board.objects.filter(title='missing').first()
>>> board = Board.objects.get(pk=1)
>>> board
<Board: 1: first>
>>> board = Board.objects.filter(id=1)
>>> board
<QuerySet [<Board: 1: first>]>
>>> boards = Board.objects.filter(title__contains='fi').all()
>>> boards
<QuerySet [<Board: 1: first>]>
>>> boards = Board.objects.filter(title__startswith='fi')
>>> boards
<QuerySet [<Board: 1: first>]>
>>> boards = Board.objects.filter(content__endswith='!')
>>> boards
<QuerySet [<Board: 1: first>, <Board: 2: second>, <Board: 3: third>, <Board: 4: fourth>]>
>>> boards = Board.objects.order_by('-title').all()
>>> boards
<QuerySet [<Board: 3: third>, <Board: 2: second>, <Board: 4: fourth>, <Board: 1: first>]>
>>> board = Board.objects.get(pk=1)
>>> board.title = 'hello'
>>> board.save()
>>> board.title
'hello'
>>> board.delete()
(1, {'boards.Board': 1})
>>> exit()
~~~

