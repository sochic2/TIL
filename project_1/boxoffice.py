import csv, requests
import json
import os


dates = ["20190113", "20190106", "20181230", "20181223", "20181216", "20181209", "20181202", "20181125", "20181118", "20181111"]
movieCd = []
movieNm = []
movieAcc = []
day = []

for date in dates:
       
    key = os.getenv("project02_key")
    url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={date}&weekGb=0'
    update = requests.get(url).json()
    for i in range(10):
        if update["boxOfficeResult"]["weeklyBoxOfficeList"][i]["movieCd"] not in movieCd:
            movieCd.append(update["boxOfficeResult"]["weeklyBoxOfficeList"][i]["movieCd"])
            movieNm.append(update["boxOfficeResult"]["weeklyBoxOfficeList"][i]["movieNm"])
            movieAcc.append(update["boxOfficeResult"]["weeklyBoxOfficeList"][i]["audiAcc"])
            day.append(date)
          
with open('boxoffice.csv','w', encoding = "UTF-8") as f:
        f.write('movie_code,title,audience,recorded_at\n')
        for i in range(len(movieCd)):
            f.write(f'{movieCd[i]},{movieNm[i]},{movieAcc[i]},{day[i]}\r')



        




