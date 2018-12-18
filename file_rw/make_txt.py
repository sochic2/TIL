# menu=["울면  ", "짬뽕  ", "라면  "]
# with open("menu2.txt", "w",encoding='utf-8') as f:
#     f.writelines(menu)

# with open("new2.txt", "r", encoding='utf-8')as f:
#     line = f.readline()
#     print(line.strip())
#     line = f.readline()
#     print(line.strip())

with open("new2.txt", "r", encoding='utf-8')as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())



# f=open("new2.txt","w")
# for i in range(1, 15):
#     data = f'{i}번째 줄입니다\t'
#     f.write(data)
# f.close()


