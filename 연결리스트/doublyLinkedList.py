class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None # 이전 노드를 가르키는 포인터
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # 맨 뒤에 노드 추가 
    def append_slow(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return 
        
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = new_node
        new_node.prev = curr

    def append_fast(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    # 맨 앞에 노드 추가
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    # 특정 노드 삭제
    def delete(self, data):
        curr = self.head
        while curr:
            if curr.data == data:

                if curr == self.head: # 삭제할 노드가 head일 때
                    self.head = curr.next
                    if self.head: self.head.prev = None
                    else: self.tail = None

                elif curr == self.tail:
                    self.tail = curr.prev
                    self.tail.next = None
                
                else:
                    curr.prev.next = curr.next # 내 앞 노드를 뒷 노드에게 전달
                    curr.next.prev = curr.prev # 내 뒷 노드를 앞 노드에게 전달

                return True
            curr = curr.next
        return False