n = 5
build_frame = 	[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]


def solution(n, build_frame):
    answer = [[]]
    result = []
    for frame in build_frame:
        x, y, structure, build = frame[0], frame[1], frame[2], frame[3]
        # 삭제
        if build == 0:
            result.remove([x, y, structure])
            true_false = check(result)
            if true_false:
                continue
            else:
                result.append([x, y, structure])



        # 설치
        else:
            result.append([x, y, structure])
            true_false = check(result)
            if true_false:
                continue
            else:
                result.pop()
    result.sort()
    return result



def check(result):
    for re in result:
        x, y, structure = re[0], re[1], re[2]
        # 기둥
        if structure == 0:
            if y == 0 or [x, y-1, 0] in result or [x, y, 1] in result or [x-1, y, 1] in result: continue
            else: return False
        # 보
        else:
            if ([x-1, y , 1] in result and [x+1, y, 1] in result) or [x, y-1, 0] in result or [x+1, y-1, 0] in result: continue
            else: return False


    return True

print(solution(n, build_frame))
