
from nodes_creation import Node

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.llsize = 0

    def push(self, data):
        '''
        This method push the elements at the end of the list O(n)
        '''
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

    def insert(self, data):
        '''
        Insert an element at the beggining of the lists O(1)
        '''
        x = Node(data, self.head)

        self.head = x


    def size(self):
        return str(self.llsize)

    def iter(self):
        '''
        Traverse the list if a head exists and until the next pointer  is None, it uses yield so remember
        to instanciate the iterator and use next on it
        '''
        current = self.head

        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        '''
        Delete the node searching the value while traversing the list.
        '''
        current = self.head
        previous = self.head

        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    previous.next = current.next
                    self.size -= 1
                    #return deleted value
                    return current.data
            
            #Move to the next node to try to find the node to be deleted
            previous = current
            current = current.next

    
    def search(self,target):
        '''You can either return  the node when you find it or just print a message that 
        it exists.
        '''
        x = self.head
        while x!=None and x.data != target:
            x = x.next

        if x != None:
            print(f'Target item {target} has been found')

        else:
            print(f'Target item {target} is not in the Linked List')

        # return x

        #Another Way
        # for node in self.iter():
        #     if target == node:
        #         print(f'Data {target} found!')


    def replace_items(self, target, data):
        '''
        Replace and item (target) of the LL with another value (data)
        '''
        x = self.head
        while x != None and x.data != target:
            x = x.next

        if x== None:
            print(f'The item {target} doesn not exist in the LL')

        else:
            x.data = data
            print(f'The item {target} has been replaced by {data}')


    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0


if __name__=='__main__':

    LL = SinglyLinkedList()
    
    
    LL.push(1)
    LL.push(5)
    LL.push(8)
    #print(LL.head.next.data)
    
    for node in LL.iter():
        print(node)

    # my_iter = LL.iter()
    # print(next(my_iter))
    # print(next(my_iter))
    # print(next(my_iter))

    print(f'Size of the LL: {LL.size()}')
    
    LL.search(5)
    
    #Replace an item in the LL
    LL.replace_items(15,"Z")
    #Print the new LL
    for node in LL.iter():
        print(node)

    print('\n')
    LL.insert(98)

    for node in LL.iter():
        print(node)
