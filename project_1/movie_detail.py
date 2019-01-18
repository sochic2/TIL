import csv, requests
import json
import os


dates = ["20190113", "20190106", "20181230", "20181223", "20181216", "20181209", "20181202", "20181125", "20181118", "20181111"]

movieCds = []
# movieCd 만들기!
for date in dates:
    key = os.getenv("project02_key")
    url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={date}&weekGb=0'
    update = requests.get(url).json()
    for i in range(10):
        if update["boxOfficeResult"]["weeklyBoxOfficeList"][i]["movieCd"] not in movieCds:
            movieCds.append(update["boxOfficeResult"]["weeklyBoxOfficeList"][i]["movieCd"])

# 나머지애들 들어갈 리스트!
movieNms = []
movieNmEns = []
movieNmOgs = []
openDts = []

genreNms = []
directors = []
watchGradeNms = []
actors_1 = []
actors_2 = []
actors_3 = []

for movieCd in movieCds:
       
    key = os.getenv("project02_key")
    url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={movieCd}'
    update = requests.get(url).json()
    movieNms.append(update["movieInfoResult"]["movieInfo"]["movieNm"])
    movieNmEns.append(update["movieInfoResult"]["movieInfo"]["movieNmEn"].replace(",","."))
    movieNmOgs.append(update["movieInfoResult"]["movieInfo"]["movieNmOg"])
    openDts.append(update["movieInfoResult"]["movieInfo"]["openDt"])
    genreNms.append(update["movieInfoResult"]["movieInfo"]["genres"][0]["genreNm"])
    directors.append(update["movieInfoResult"]["movieInfo"]["directors"][0]["peopleNm"])
    watchGradeNms.append(update["movieInfoResult"]["movieInfo"]["audits"][0]["watchGradeNm"])
    if len(update["movieInfoResult"]["movieInfo"]["actors"]) >=1:
        actors_1.append(update["movieInfoResult"]["movieInfo"]["actors"][0]["peopleNm"])
    else:
        actors_1 += [""]
    if len(update["movieInfoResult"]["movieInfo"]["actors"]) >= 2:
        actors_2.append(update["movieInfoResult"]["movieInfo"]["actors"][1]["peopleNm"])
    else:
        actors_2 += [""]
    if len(update["movieInfoResult"]["movieInfo"]["actors"]) >=3:
        actors_3.append(update["movieInfoResult"]["movieInfo"]["actors"][2]["peopleNm"])
    else:
        actors_3 += [""]

# print(movieCds)
# print(movieNms)
# print(movieNmEns)
# print(movieNmOgs)
# print(openDts)
# print(showTms)
# print(genreNms)
# print(directors)
# print(watchGradeNms)
# print(actors_1)
# print(actors_2)
# print(actors_3) 

with open('movie.csv','w', encoding = "UTF-8") as f:
        f.write('movie_code,movie_name_ko,movie_name_en,movie_name_og,prdt_year,genres,directors,watch_grade_nm,actor1,actor2,actor3\n')
        for i in range(len(movieCds)):
            f.write(f'{movieCds[i]},{movieNms[i]},{movieNmEns[i]},{movieNmOgs[i]},{openDts[i]},{genreNms[i]},{directors[i]},{watchGradeNms[i]},{actors_1[i]},{actors_2[i]},{actors_3[i]}\r')

