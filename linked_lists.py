
from nodes_creation import Node

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.llsize = 0

    def push(self, data):
        node = Node(data)

        #Check if your LL has Nodes already if not  it starts assigning a head
        if self.head == None:
            self.head = node
        else:
            current = self.head

            #Adding the object at the end of the LL
            while current.next:
                current = current.next

            current.next = node
        
        self.llsize += 1

    def size(self):
        return str(self.llsize)

    def iter(self):
        current = self.head

        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        current = self.tail
        previous = self.tail

        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    previous.next = current.next
                    self.size -= 1
                    #return deleted value
                    return current.data
            
            previous = current
            current = current.next


if __name__=='__main__':

    LL = SinglyLinkedList()
    
    
    LL.push(1)
    LL.push(5)
    LL.push(8)
    print(LL.head.next.data)
    
    
    my_iter = LL.iter()
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))

    print(LL.size())
    


                