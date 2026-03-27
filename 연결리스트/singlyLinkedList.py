class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singlyLinkedList:
    def __init__(self):
        self.head = Node
        self.tail = Node
    
    # 연결리스트 출력하기
    def display(self): # 헤드부터 마지막 노드까지 이동하며 출력, 마지막 노드는 None을 가르키기 때문에 None이 아닐때까지 출력
        curr = self.head # 헤드가 이동하면 연결리스트를 잃기 때문에 변수 사용

        while curr:
            print(curr.data, end=" -> " if curr.next else "")
            curr = curr.next
        print()
    
    # 마지막 노드에 새 노드 추가하기
    def append_slow(self, data): # 모든 노드를 지나기 때문에 시간복잡도 O(n)
        new_node = Node(data)

        if not self.head: # 리스트가 비어있을 때
            self.head = new_node
            self.tail = new_node
            return

        curr = self.head # 마지막 노드로 이동
        while curr.next:
            curr = curr.next

        curr.next = new_node
        self.tail = new_node
    
    def append_fast(self, data): # tail을 사용해서 시간복잡도 O(1)
        new_node = Node(data)

        if not self.head: # 리스트가 비어있을 때
            self.head = new_node
            self.tail = new_node
            return
        
        self.tail.next = new_node
        self.tail = new_node

    # 첫 번째 노드에 새 노드 추가하기
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
    
    # 특정 값 삭제하기
    def delete(self, data):
        if not self.head: return
        
        if self.head.data == data: # 삭제하려는 값이 헤드일 때 
            self.head = self.head.next

            if not self.head: # 리스트가 비는지 확인
                self.tail = None
                return

        curr = self.head
        while curr.next:
            if curr.next.data == data:
                if curr.next == self.tail:
                    self.tail = curr

                curr.next = curr.next.next
                return
            curr = curr.next
                
    # 리스트 뒤집기
    def reverse(self):
        prev = None 
        curr = self.head
        self.tail = self.head 

        while curr:
            next_node = curr.next # 다음 노드를 먼저 저장
            curr.next = prev # 현재 노드의 화살표를 뒤로 꺾기
            prev = curr # 다음 노드로 이동
            curr = next_node 
        
        self.head = prev    

    # 노드 위치 찾기
    def get_node_at(self, index):
        if index < 0:
            return None
        
        curr = self.head
        count = 0

        while curr is not None and count < index:
            curr = curr.next
            count += 1
        
        return curr