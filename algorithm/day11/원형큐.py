# queue = []
# queue.append(1)
# queue.append(2)
# queue.append(3)
# print(queue.pop(0))
# print(queue.pop(0))
# print(queue.pop(0))
SIZE = 4
Q = [0] * SIZE
front, rear = 0, 0
def isFull():
    global rear, front
    return (rear+1) % len(Q) == front

def isEmpty():
    global front, rear
    return front == rear

# def enQue(item):
#     global rear, front
#     if isFull(): print("Queue Full")
#     else:
#         rear += 1
#         Q[rear%SIZE] = item
#
# def deQueue():
#     global front, rear
#     front +=1
#     return Q[front%SIZE]
def enQue(item):
    global rear
    if isFull(): print("Queue Full")
    else:
        rear = (rear+1) % len(Q)
        Q[rear] = item
def deQueue():
    global front
    if isEmpty(): print("Queue Empty")
    else:
        front = (front+1) % len(Q)
        return Q[front]




isEmpty()
enQue(1)
enQue(2)
enQue(3)
print(deQueue())
print(deQueue())
print(deQueue())
enQue(4)
print(deQueue())
enQue(5)
print(deQueue())
print(Q)
