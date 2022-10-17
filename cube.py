#Create a 3D Array
import random
#from array import Array
#from grid  import Grid

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
            
    
class Grid():
    '''
    Class created to represent Multidimensional arrays
    '''
    #Remember that fill_value is created in order to assign default values to the elements of the array
    def __init__(self, rows, columns, fill_value=None):
        '''
        At the end of the constructor you will have an object of dimensions ROWSxCOLUMNS
        '''
        #Assign an array of size rows to the attribure data
        self.data = Array(rows)

        for row in range(rows):
            #For each row set an array of N number of columns (The size of each Array will be the same because columns is constant)
            self.data[row] = Array(columns, fill_value)

    #Array Length, is just for query that's why it's private
    def __len__(self):
        return len(self.data)
    

    def get_height(self):
        '''
        Get the number of rows of the grid
        '''
        return len(self.data)

    def get_width(self):
        '''
        Get the number of columns of the grid
        '''
        return len(self.data[0])

    def __getitem__(self, index):
        return self.data[index]

    def __str__(self):
        result = ""
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col]) + " "

            result += "\n"
        
        return str(result)

    #Generate an interator to go through the elements of the array
    
    def __iter__(self):
        '''
        Remember that an iterable can become an iterator with the iter() method
        '''
        return iter(self.data)

    def replace_items(self):
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                self.data[row][col] = random.randint(0,100)


        

class Cube:
    '''
    Class to represent a 3D array
    '''
    def __init__(self, rows, cols, dims, fill_value = 10):
        self.info = Grid(rows, cols)
        print(self.info)
        for row in range(rows):
            for col in range(cols):
                self.info[row][col] = Array(dims, fill_value)

    def __getitem__(self, index):
        return self.info[index]


if __name__=='__main__':
    rows = int(input('Introduce the number of rows: '))
    cols = int(input('Introduce the number of columns: '))
    steps = int(input('Introduce the number of steps in the third Dimensions: '))

    td_matrix = Cube(rows, cols, steps)

    print(f'Welcome to the TENSOR: {td_matrix}')
    print(td_matrix[0][1][3])