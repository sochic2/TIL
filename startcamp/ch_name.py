#외장함수 os 불러오기
import os
#저장된 위치로 이동하기
os.chdir(r"C:\Users\student\Desktop\TIL\dummy")
#이미 그 위치에 있으니까 위치는 . 
for filename in os.listdir("."):
    os.rename(filename, filename.replace("SAMSUNG SAMSUNG","SSAFY"))



