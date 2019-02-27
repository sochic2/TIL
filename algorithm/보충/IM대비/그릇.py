#
# data = '()()()(((())()'
# result_list = []
# result = 0
# for i in data:
#     if i == '(' :
#         if len(result_list) != 0 and result_list[-1] == '(':
#             result += 5
#         else:
#             result += 10
#
#     if i == ')':
#         if len(result_list) != 0 and result_list[-1] == ')':
#             result += 5
#         else:
#             result += 10
#
#     result_list.append(i)
# print(result)





data = input()
result = 10
for i in range(1, len(data)):
    if data[i-1] != data[i]:
        result += 10
    else:
        result += 5

print(result)




