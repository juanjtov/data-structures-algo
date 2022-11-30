from array import Array 
from linked_lists import SinglyLinkedList




if __name__=='__main__':

    #Create array
    arr_dimen = int(input('Insert how many items would you like in the array: '))
    #Array with none values
    new_arr = Array(arr_dimen)
    #Fill the array with random numbers from 0 to 500
    new_arr.__replacingitems__()
    print(new_arr)
    #Instanciate the LL
    LL = SinglyLinkedList()
    
    #Traverse the array and push the items into the LL
    for i in range(len(new_arr)):
        LL.push(new_arr[i])

    #Print the linked list
    for node in LL.iter():
        print(node)