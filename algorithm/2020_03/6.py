







def solution(directory, command):
    answer = []
    for i in directory:
        answer.append(i)

    for com in command:
        order = com.split()[0]
        if order == 'mkdir':
            answer.append(com.split()[1])

        if order == 'cp':
            dir1 = com.split()[1]
            dir2 = com.split()[2]
            split_dir1 = dir1.split('/')
            result = []
            for ans in answer:
                split_ans = ans.split('/')
                flag = 0
                for i in range(len(split_dir1)):
                    if split_ans[i] != split_dir1[i]:
                        flag = 1
                if flag == 0:
                    result.append(dir2 + ans)
            answer += result
            answer.sort()


        if order == 'rm':
            remove_list = []
            dir = com.split()[1]
            split_dir = dir.split('/')
            for ans in answer:
                split_ans = ans.split('/')

                flag = 0
                for i in range(len(split_dir)):
                    if split_ans[i] != split_dir[i]:
                        flag = 1
                if flag == 0:
                    remove_list.append(ans)
            for z in remove_list:
                answer.remove(z)



    answer.sort()
    return answer

directory = [
"/",
"/hello",
"/hello/tmp",
"/root",
"/root/abcd",
"/root/abcd/etc",
"/root/abcd/hello"
]

command = [
"mkdir /root/tmp",
"cp /hello /root/tmp",
"rm /hello"
]

print(solution(directory, command))