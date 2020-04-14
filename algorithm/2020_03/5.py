def solution(dataSource, tags):
    docs = []
    answer = []
    for data in dataSource:
        doc = data[0]
        cnt = 0
        for tag in tags:
            if tag in data:
                cnt += 1
        if cnt > 0:
            if len(docs) >= 10:
                if docs[9][0] < cnt:
                    docs[9] = [cnt, doc]
            else:
                docs.append([cnt, doc])
            docs = sorted(docs, key= lambda x : x[0], reverse=True)
    for doc in docs:
        answer.append(doc[1])
    return answer

print(solution([
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"],
    ["doc6", "t1"],
    ["doc7", "t1", "t2", "t3"],
["doc8", "t1", "t2", "t3"],
["doc9", "t1", "t2", "t3"],
["doc10", "t1", "t2", "t3"],
["doc11", "t1", "t2", "t3"],
["doc12", "t1", "t2", "t3"],
    ["doc13", "t1", "t2", "t3"],
    ["doc14", "t1", "t2", "t3"],
["doc15", "t1", "t2", "t3"],
["doc16", "t1", "t2", "t3"],
    ["doc17", "t1", "t2", "t3"],
["doc18", "t1", "t2", "t3"],
["doc19", "t1", "t2", "t3"],
    ["doc20", "t1", "t2", "t3"],
["doc21", "t1", "t2", "t3"],
["doc22", "t1", "t2", "t3"],
["doc23", "t1", "t2", "t3", "t4"],








], ["t1", "t2", "t3", "t4"]))