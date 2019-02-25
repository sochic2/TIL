# queue = []
# queue.append(1)
# queue.append(2)
# queue.append(3)
# print(queue.pop(0))
# print(queue.pop(0))
# print(queue.pop(0))
SIZE = 100
Q = [0] * SIZE
front, rear = -1, -1
def isFull():
    global rear
    return rear == len(Q)-1

def isEmpty():
    global front, rear
    return front == rear

def enQue(item):
    global rear
    if isFull(): print("Queue Full")
    else:
        rear += 1
        Q[rear] = item

def deQueue():
    global front, rear
    front +=1
    return Q[front]


isEmpty()
enQue(1)
enQue(2)
enQue(3)
print(deQueue())
print(deQueue())
print(deQueue())