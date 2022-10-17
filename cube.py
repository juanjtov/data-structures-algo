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

    def __getitem__(self, index):
        return self.info[index]

    def __str__(self):
        return str(self.info)


if __name__=='__main__':
    rows = int(input('Introduce the number of rows: '))
    cols = int(input('Introduce the number of columns: '))
    steps = int(input('Introduce the number of steps in the third Dimensions: '))

    td_matrix = Cube(rows, cols, steps)

    print(f'Welcome to the TENSOR: {td_matrix}')
    