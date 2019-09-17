# README

# 1. 팀원 구성

- ### 김구현

- ### 남기철

  ### 1-1. 역할 구성

| 김구현     | DATABASE 수집을 위한 Python Code 작성      | CSS와 VUE 를 활용한 Front-End Design |
| ---------- | ------------------------------------------ | ------------------------------------ |
| **남기철** | **추천 시스템 구상을 위한 Algorithm 작성** | **서버 전체적인 Back-End**           |

# 2. 페이지 제작

### 1. 목표 서비스 구현 및 실제 구현 정도

### 	1-1. DATABASE 수집을 위한 API CRAWLING CODE 작성

```python
from bs4 import BeautifulSoup as bts
from datetime import datetime, timedelta
import csv, requests, os, json
from pprint import pprint

API = os.getenv("API_TOKEN")

with open('boxoffice.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ('movie_id', 'movie_title',)
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    m_list = []
    mo_ko_name = []
    for j in range(5, 500):
        url = f'https://api.themoviedb.org/3/movie/popular?{API}&language=ko-KR&page={j}'
        req = requests.get(url).json()
        for i in range(20):
            m_info = req["results"][i]
            if m_info["id"] not in m_list:
                m_list.append(m_info["id"])
                mo_ko_name.append([m_info['id'], m_info['title']])
                code = writer.writerow({'movie_id': m_info["id"], 
                                        'movie_title': m_info["title"],})

with open('boxoffice.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip().split(','))

with open('movie.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ('id','adult', 'budget', 'genres', 'original_title', 'overview', 'popularity', 'poster_path', 'release_date', 'revenue', 'runtime', 'tagline', 'title', 'actor_1', 'actor_2', 'actor_3', 'director', 'file_path_1', 'file_path_2', 'file_path_3')
    words = ['adult', 'budget', 'genres', 'original_title', 'overview', 'popularity', 'poster_path', 'release_date', 'revenue', 'runtime', 'tagline', 'title']
    actor_list = []
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    ccount = 1
    for j in range(len(m_list)):
        url = f'https://api.themoviedb.org/3/movie/{m_list[j]}?{API}&language=ko-KR'
        req = requests.get(url).json()
        m_info = req
        solution = {'id':ccount, 'adult':"N/A", 'budget':"N/A", 'genres':"N/A", 'original_title':"N/A", 'overview':"N/A", 'popularity':"N/A", 'poster_path':"N/A", 'release_date':"N/A", 'revenue':"N/A", 'runtime':"N/A", 'tagline':"N/A", 'title':"N/A", 'actor_1':"N/A", 'actor_2':"N/A", 'actor_3':"N/A", 'director':"", 'file_path_1':"N/A", 'file_path_2':"N/A", 'file_path_3':"N/A", }
        ccount += 1
        for T in words:
            if m_info[T]:
                if T == "genres":
                    for gre in range(len(m_info[T])):
                        solution[T] = m_info["genres"][gre]['id']
                else:
                    solution[T] = m_info[T]
            else:
                solution[T] = "N/A"

            
                    
        url = f'https://api.themoviedb.org/3/movie/{m_list[j]}/credits?{API}'
        req = requests.get(url).json()
        m_info = req
        if m_info["cast"]:
            if len(m_info['cast']) >= 3:
                for actor_index in range(3):
                    if m_info['cast'][actor_index]['id'] not in actor_list:
                        actor_list.append({'actor_id': m_info['cast'][actor_index]['id'], 'actor_name':m_info['cast'][actor_index]['name']})
                if m_info['cast']:
                    solution['actor_1'] = m_info['cast'][0]['id']
                    solution['actor_2'] = m_info['cast'][1]['id']
                    solution['actor_3'] = m_info['cast'][2]['id']
        else:
            solution['actor_1'] = "N/A"
            solution['actor_2'] = "N/A"
            solution['actor_3'] = "N/A" 
        
        if m_info['crew']:
            solution['director'] = m_info['crew'][0]['name']

        url = f'https://api.themoviedb.org/3/movie/{m_list[j]}/images?{API}'
        req = requests.get(url).json()
        m_info = req["backdrops"]
        if len(m_info) >= 3:
            solution['file_path_1'] = m_info[0]['file_path']
            solution['file_path_2'] = m_info[1]['file_path']
            solution['file_path_3'] = m_info[2]['file_path']
        else:   
            solution['file_path_1'] = "N/A"
            solution['file_path_2'] = "N/A"
            solution['file_path_3'] = "N/A"
        
        writer.writerow({'adult' : solution['adult'],
                        'genres' : solution['genres'],
                        'budget' : solution['budget'],
                        'id' : solution['id'],
                        'original_title' : solution['original_title'],
                        'overview' : solution['overview'],
                        'popularity' : solution['popularity'],
                        'poster_path' : solution['poster_path'],
                        'release_date' : solution['release_date'],
                        'revenue' : solution['revenue'],
                        'runtime' : solution['runtime'],
                        'tagline' : solution['tagline'],
                        'title' : solution['title'],
                        'actor_1' : solution['actor_1'],
                        'actor_2' : solution['actor_2'],
                        'actor_3' : solution['actor_3'],
                        'director' : solution['director'],
                        'file_path_1' : solution['file_path_1'],
                        'file_path_2' : solution['file_path_2'],
                        'file_path_3' : solution['file_path_3']},
                        )

with open('movie.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip().split(','))

with open('genres.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ('id','name','genre_box_id')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    
    ccount = 0
    for j in range(19):
        url = f'https://api.themoviedb.org/3/genre/movie/list?{API}&language=ko-KR'
        req = requests.get(url).json()
        m_info = req['genres']
        ccount += 1
        writer.writerow({'id' : ccount,
            'name' : m_info[j]['name'],
            'genre_box_id' : m_info[j]['id']})

with open('actor_list.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ('id','actor_id','actor_name')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    
    ccount = 0
    for j in range(len(actor_list)):
        ccount += 1
        writer.writerow({'id' : ccount,
            'actor_id' : actor_list[j]['actor_id'],
            'actor_name' : actor_list[j]['actor_name']})

```

- #### THE MOVIE DATABASE API 를 활용하여 영화 데이터를 불러왔다.

- #### 원하는 정보와 TMDB API에서 제공하는 정보들이 일치하지 않거나 부족한 경우가 많았다.

  - API 에서 제공하는 정보들을 하나 이상의 페이지에서 종합적으로 수집하기 위해 여러번의 수정을 거치며 JSON 형식과 CSV 형식을 모두 활용해 보았으며, 최종적을 CSV를 활용하는 방안으로 방향을 정하였다.
  - 초기에는 모든 정보를 하나의 CSV에 저장하였으나, 이후 더 정확한 정보 수집을 위하여 MOVIEDETAIL 과 GENRE, ACTOR 3개의 파일로 나누어 저장하였다.
  - 이를 통해, 각 정보에 대한 정확도가 증가하였으며 더 많은 정보를 사용할 수 있게 되었다.
  - 특히, InetegerField 와 TextField를 선정하는데 있어 많은 어려움이 있었으나 최종적으로 TextField 로 수집하였고, 이후 DB에 저장된 정보를 Python 코드에서 변형하여 활용하였다.

- `출처 :` `<https://developers.themoviedb.org/3>` 

  ### 1-2. 다양한 영화 정보 수집을 목표로

  - #### 초기 사이트 구상은 영화에 대한 많은 정보를 기반으로 읽을거리가 많은 사이트를 만드는 것을 목표로 하였다.

    ```
    1. 영화와 관련된 이야기 거리들
    	- 수많은 블로거들이 남긴 후기를 즉시 읽을 수 있도록 구상
    	- 리뷰이외의 영화 제작 비하인드 스토리나 영화에 숨어 있는 요소들을 소개시켜 주는 페이지
    	- 영화 배우들의 인터뷰 등
    2. 영화에 대한 사전정보 수집
    	- 단순 영화를 관람하기보다 영화의 배경지식을 알 수 있다면 더욱 흥미롭지 않을까 하는 생각
    	- 역사적 사실에 대한 이야기와 영화에서 변경된 내용들을 알 수 있다면 좋겠다.
    	- 배우 캐스팅 중에 생겼던 헤프닝 등
    ```

    - 그러나 본 예상보다 사이트 구성을 위한 코드 작성에 어려움을 겪었고, 최종적으로는 기본 설정에 집중하는 방향으로 나아가기로 하였다.

      ```
      1. 유저가 리뷰를 남긴 정보를 활용하여 영화 추천 서비스
      	- 유저가 선호하는 장르를 기반으로 10개의 영화를 추천
      2. 세계적인 유명도와 고 예산 영화 추천
      ```

      

## 2. 데이터베이스 모델링

![er관계](https://user-images.githubusercontent.com/45934115/57836504-d117b800-77fb-11e9-8f92-046e44bb24e3.png)

## 3. 핵심 기능

- ### 영화 상세 정보

  ## ![detail](https://user-images.githubusercontent.com/45934115/57836670-323f8b80-77fc-11e9-912e-b6fb8dd2badb.PNG)

- ### 리뷰 작성

  ![detail2](https://user-images.githubusercontent.com/45934115/57836696-41263e00-77fc-11e9-92b9-2a15b629cc28.PNG)

- ### 장르별 영화 목록

  ![genre](https://user-images.githubusercontent.com/45934115/57836722-4c796980-77fc-11e9-894b-4e4994f75dbd.PNG)

- ### 선호하는 유저와의 관계형성

  ![profile](https://user-images.githubusercontent.com/45934115/57836868-95312280-77fc-11e9-90fc-0b7fe0b63986.PNG)

- ### 선호하는 장르와 일치하는 영화 추천

  ![ratingmain](https://user-images.githubusercontent.com/45934115/57836886-a11ce480-77fc-11e9-9b22-2834829af79f.PNG)

  

### 4. 배포 서버 URL

- ### <https://django-project-rngus3050.c9users.io/>



### 5. 느낀점

| 남기철                                                       |                            김구현                            |
| :----------------------------------------------------------- | :----------------------------------------------------------: |
| DJANGO 에서 제공해주는 각종 기능에 대해 조금 더 긍정적인 생각을 가지게 되었다. 특히, 기본적인 요소 들에 대한 다양한 지원이 앞으로의 서버 개발이나 페이지 구축에 있어 큰 힘이 될 것이라는 생각이 들었다.<br />VUE를 활용 하여 JAVASCRIPT를 작성하는 것에는 수업 때보다 많은 것들을 활용하려다 보니 역량 부족이 크게 다가왔다. 무엇보다 JS의 큰 장점인 비동기를 활용하지 못한 부분이 너무 아쉽게 느껴졌다. JS에 대한 이해도를 더욱 높인다면 기존에 제작한 페이지보다 더욱 화려하고 실용적인 기능들을 구현할 수 있을 것 같아 앞으로의 공부에 큰 원동력이 되었다. | 프로젝트를  진행하기 전에는 Front-End 에 대한 막연한 자신감이 있었다. 그러나 직접 진행함에 있어서는 예상외의 문제점들이 많이 발생하였고, 이를 구현하기 위한 코드를 작성 할 때  Document 를 제대로 활용하지 못한다는 문제점을 발견하였다. <br />앞으로는 조금 더 많은 정보를 활용 할 수 있는 실력을 기를 필요가 있다고 생각 되었다. 특히, CSS 뿐만 아니라 JS 를 활용하였을 때, 평소에는 아무렇지 않게 사용하던 다양한 기능들을 구현할 수 있다는 것을 알게 되었고 이에 대한 기대감이 매우 높아졌다. |



