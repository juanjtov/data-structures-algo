#Create a 3D Array
import random
from array import Array
from grid  import Grid


class Cube:
    '''
    Class to represent a 3D array
    '''
    def __init__(self, rows, cols, dims, fill_value = None):
        self.info = Grid(rows, cols)
        print(self.info)
        for row in range(rows):
            for col in range(cols):
                self.info[row][col] = Array(dims, fill_value)

    def get_height(self):
        '''Returns the number of rows'''
        return len(self.info)

    def get_width(self):
        '''Returns the number of columns'''
        return len(self.info[0])

    def get_depth(self):
        '''Return the depth of the 3D dimension'''
        return len(self.info[0][0])


    def __getitem__(self, index):
        return self.info[index]

    def __str__(self):
        #for dim in 



        return str(self.info)



if __name__=='__main__':
    rows = int(input('Introduce the number of rows: '))
    cols = int(input('Introduce the number of columns: '))
    steps = int(input('Introduce the number of steps in the third Dimensions: '))

    td_matrix = Cube(rows, cols, steps)

    print(f'Welcome to the TENSOR: {td_matrix}')
    