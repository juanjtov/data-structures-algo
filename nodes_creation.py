
class Node:

    def __init__(self, data,  next=None) -> None:
        self.data = data
        self.next = next
        #self.prev = prev
        


if __name__=='__main__':
    
    node2 = Node("A", None)
    node3 = Node("B", node2)
    node1 = Node("C", node3)
    print(f'Node in node 2: {node2.data}')
    print(f'Node after node3: {node3.next.data}')
    print(f'Node after node1: {node1.next.data}')

    #Creating a linked list
    head = None
    for count in range(1, 5):
        head = Node(count, head)
    
    while head != None:
        print(head.data)
        head = head.next
