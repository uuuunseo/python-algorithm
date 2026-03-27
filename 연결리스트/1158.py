class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n, k = map(int, input().split())

def phus(n, k):
    head = Node(1)
    prev = head
    
    for i in range(2, n+1):
        curr = Node(i)
        prev.next = curr
        prev = curr
    prev.next = head

    curr = head
    prev = prev
    result = []

    while curr.next != curr:
        for _ in range(k - 1):
            prev = curr
            curr = curr.next
        
        result.append(curr.data)
        prev.next = curr.next
        curr = prev.next
    
    result.append(curr.data)
    return result

result = phus(n, k)
print("<", end="")
print(*result, sep=", ", end="")
print(">")