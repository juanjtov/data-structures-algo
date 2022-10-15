
import random

class Array:
    '''
    Define an array an its methods. All the "Dunder score items" are magical methods, then you can cast them as 
    Python built-in methods as: str(), getitem(), len()
    '''
    def __init__(self, capacity, fill_value = None):
        self.items = list ()
        self.capacity = capacity
        for _ in range(self.capacity):
            self.items.append(fill_value)

    #Array Length, is just for query that's why it's private
    def __len__(self):
        return len(self.items)

    #Return the array as a string
    def __str__(self):
        return str(self.items)

    #Generate an interator to go through the elements of the array
    
    def __iter__(self):
        '''
        Remember that an iterable can become an iterator with the iter() method
        '''
        return iter(self.items)

    #Get one item of the array

    def __getitem__(self, index):
        '''
        Search items in an Array has complexity O(c)
        '''
        return self.items[index]
    
    
    #Inster element in an Array
    def __setitem__(self, index, new_item):
        '''
        Insert elements in an Array has complexity O(c)
        '''
        self.items[index] = new_item

    def __replacingitems__(self):
        
        #Standard For
        # for i in range(self.capacity):
        #     self.__setitem__(i, random.randint(0,500))

        #Using list comprenhensions
        return [self.__setitem__(i, random.randint(0,500)) for i in range(self.capacity)]


    #####################Regular Methods
    
    #Using the convencional way
    
    def replaceitems(self):
        '''
        Filling the array with random numbers
        '''
        for i in range(len(self.items)):
            self.items[i] = random.random()

    def sum_values(self):
        '''
        Add all the values of the array
        '''
        sum_v = 0
        for i in range(len(self.items)):
            sum_v = sum_v + self.items[i]
        
        return sum_v
            
    

if __name__=='__main__':
    arr_capacity = int(input('Insert the array capacity: '))
    menu = Array(arr_capacity)
    len(menu)
    print(menu)
    print(f'The lenght of the array is: {menu.__len__()}')
    #fill the elements
    # for i in range(menu.__len__()):
    #     menu[i] = i+5

    print(menu)
    #Query the items of the array
    for option in menu:
        print(option)

    print(str(menu))
    print(f'Array being called directly using the .__str__  method: {menu.__str__()}, {type(menu.__str__())}')
    print(type('Hi sweetie'))

    print(f'Using __getitem__(3): {menu.__getitem__(3)}')

    #Setting a new item in the position of the index 1, new item is 100: 
    menu.__setitem__(1,100)
    print(menu)

    menu.replaceitems()
    print(f'Menu when the items have been replaced: {menu}')

    print(f'Adding all the values of the array using sum_values(): {menu.sum_values()}')

    print('Replacing items using magical methods and randint:\n')
    menu.__replacingitems__()
    #####When I print the method being executed the result is [None,None, etc.]
    #print(menu.__replacingitems__())

    #These two prints are the same
    print(menu.__str__())
    print(menu)