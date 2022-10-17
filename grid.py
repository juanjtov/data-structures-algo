#Multi Dimension Arrays

import random
from array import Array

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
        return iter(self.items)

    def replace_items(self):
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                self.data[row][col] = random.randint(0,100)


                



if __name__=='__main__':
    x = int(input('Inseet the number of rows: '))
    y = int (input('Insert the number of columns: '))
    matrix = Grid(x,y)
    print(matrix, type(matrix))
    print('\n')
    matrix.replace_items()
    print(f'Matrix when the numbers have been replaced : \n{matrix}')