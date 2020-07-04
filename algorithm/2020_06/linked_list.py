class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList 클래스 (자료구조) 정의
class LinkedList:

    # 초기화 메소드
    def __init__(self):
        dummy = Node("dummy")
        self.head = dummy
        self.tail = dummy

        self.current = None
        self.before = None

        self.num_of_data = 0

    # append 메소드 (insert - 맨 뒤에 노드 추가, tail과 node의 next, 데이터 개수 변경)
    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

        self.num_of_data += 1

    # delete 메소드 (delete - current 노드 삭제, 인접 노드의 current, next 변경, 데이터 개수 변경)
    def delete(self):
        pop_data = self.current.data

        if self.current is self.tail:
            self.tail = self.before

        self.before.next = self.current.next
        self.current = self.before  # 중요 : current가 next가 아닌 before로 변경된다.
        #

        self.num_of_data -= 1

        return pop_data

    # first 메소드 (search1 - 맨 앞의 노드 검색, before, current 변경)
    def first(self):
        if self.num_of_data == 0:  # 데이터가 없는 경우 첫번째 노드도 없기 때문에 None 리턴
            return None

        self.before = self.head
        self.current = self.head.next

        return self.current.data

    # next 메소드 (search2 - current 노드의 다음 노드 검색, 이전에 first 메소드가 한번은 실행되어야 함)
    def next(self):
        if self.current.next == None:
            return None

        self.before = self.current
        self.current = self.current.next

        return self.current.data

    def size(self):
        return self.num_of_data


###################
if __name__ == '__main__':
    l_list = LinkedList()
    l_list.append(5)
    l_list.append(2)
    l_list.append(1)
    l_list.append(2)
    l_list.append(7)
    l_list.append(2)
    l_list.append(11)

    print('first :', l_list.first())  # first : 5
    print('next :', l_list.next())  # next : 2
    print('size :', l_list.size())  # size : 7
    print('delete :', l_list.delete())  # delete : 2
    print('size :', l_list.size())  # size : 6
    print('current:', l_list.current.data)  # current: 5
    print('tail:', l_list.tail.data)  # tail: 11
    print('first :', l_list.first())  # first : 5
    print('next :', l_list.next())  # next : 1
    print('next :', l_list.next())  # next : 2
    print('next :', l_list.next())  # next : 7

    # 전체 노드 data 표시하기
    data = l_list.first()

    if data:
        print(data, end=' ')
        while True:
            data = l_list.next()
            if data:
                print(data, end= ' ')
            else:
                break
        # 5 1 2 7 2 11

        # 2만 삭제하기
    data = l_list.first()

    if data and data == 2:
        l_list.delete()
        print('deleted', end=' ')
    else:
        print(data, end= ' ')

    while True:
        data = l_list.next()
        if data == 2:
            l_list.delete()
            print('deleted', end=' ')
        elif data:
            print(data, end=' ')
        else:
            break

    # 5 1 deleted 7 deleted 11
