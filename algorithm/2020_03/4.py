def solution(snapshots, transactions):
    answer = []
    accounts = {}
    chk = [0] * 111111
    for snapshot in snapshots:
        id = snapshot[0]
        money = int(snapshot[1])
        accounts[id] = money

    for transaction in transactions:
        id2 = int(transaction[0])
        status = transaction[1]
        id = transaction[2]
        money = int(transaction[3])
        if chk[id2]:continue
        if id not in accounts:
            accounts[id] = 0

        if status == 'SAVE':
            accounts[id] += money
        else:
            accounts[id] -= money
        chk[id2] = 1

    for key, value in accounts.items():
        answer.append([key, str(value)])




    answer.sort()

    return answer

print(solution([
["ACCOUNT2", "150"],
  ["ACCOUNT1", "100"],

],
    [
        ["1", "SAVE", "ACCOUNT2", "100"],
        ["2", "WITHDRAW", "ACCOUNT1", "50"],
        ["1", "SAVE", "ACCOUNT2", "100"],
        ["4", "SAVE", "ACCOUNT3", "500"],
        ["3", "WITHDRAW", "ACCOUNT2", "30"]
    ]
))