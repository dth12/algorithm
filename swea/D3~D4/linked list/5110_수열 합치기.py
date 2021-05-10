import sys
sys.stdin = open("input.txt", "r")

class Node:
    def __init__(self, item, prev = None, next = None):
        self.item = item
        self.prev = prev
        self.next =next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        if self.size:
            return False
        else:
            return True

    def select(self, idx):
        if idx >= self.size or idx < 0:
            print('overflow')
            return None
        elif idx <= self.size // 2:
            selected = self.head
            for _ in range(idx):
                selected = selected.next
            return selected
        elif idx > self.size // 2:
            selected = self.tail
            for _ in range(self.size-idx-1):
                selected = selected.prev
            return selected

    def append(self, item):
        if self.is_empty():
            self.head = Node(item)
            self.tail = self.head
        else:
            before = self.tail
            self.tail = Node(item, prev=before)
            before.next = self.tail
        self.size += 1

    def insert(self, item, idx):
        if idx >= self.size or idx < 0:
            print('overflow')
            return None

        if self.is_empty():
            self.head = Node(item)
            self.tail = self.head
        else:
            # 0 1 2 item 3
            temp = self.select(idx)
            new_node = Node(item, prev=temp.prev, next=temp)
            if idx == 0:
                temp.prev = new_node
                self.head = new_node
            else:
                temp.prev.next = new_node
                temp.prev = new_node

        self.size += 1

    def last_ten(self):
        return_list = []
        target = self.tail
        for _ in range(10):
            return_list.append(target.item)
            target = target.prev

        return return_list

    def find_large(self, value):
        target = self.head
        for idx in range(self.size):
            if target.item > value:
                return idx
            else:
                target = target.next

        return self.size


    def printList(self):
        return_val = ''
        target = self.head
        for _ in range(self.size):
            return_val += str(target.item) + ' => '
            target = target.next
        return return_val


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    linked = LinkedList()
    first = list(map(int, input().split()))
    for i in first:
        linked.append(i)

    for i in range(M-1):

        temp_list = list(map(int, input().split()))
        idx = linked.find_large(temp_list[0])
        if idx == linked.size:
            for num in temp_list:
                linked.append(num)
        else:
            for num in temp_list[::-1]:
                linked.insert(num, idx)

    print('#{}'.format(tc), *linked.last_ten())




