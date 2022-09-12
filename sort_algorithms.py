import random
import time
import copy

def func_timer(func):
    
    def wrapper(*args, **kwargs):
        initial_time = time.time()
        finded = func(*args, **kwargs)
        final_time = time.time()
        duration = final_time - initial_time
        print('The algorithm {} took {} seconds to be executed'.format(func.__name__, duration))
        return finded

    return wrapper

@func_timer
def bubble_sort(array):
    #In the first loop you can find the maximum value
    n = len(array)

    for i in range(n):
        for j in range(0, n - i - 1):

            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array


@func_timer
def insertion_Sort(array):
    if array:                                                  #c1
        for j in range(1, len(array)):                         #c2 :  (n-1)times    
            key = array[j]                                     #c3 :  (n-1)times
            #Insert A[j] into the sorted array A[1...j-1]
            i = j-1                                            #c4 :  (n-1)times    
            while i >= 0 and array[i] > key:                    #c5:   Best case - 0 times  Worst case - summation(from 2 to n) times 
                array[i+1] = array[i]                          #c6:   Best case - 0 times  Worst case - summation(from 2 to n) times 
                i = i-1                                        #c7:   Best case - 0 times  Worst case - summation(from 2 to n) times 
            
            array[i+1] = key                                   #c8:   (n-1) times
        
        return array
    else:
        print('The input array is empty')


def merge_sort(array):
    
    if len(array) > 1:
        med = len(array) // 2
        left_side = array[:med] #desde el principio del array hasta la mitad
        right_side = array[med:] #desde la mitad hasta el final

        #print('This is the left side before recursion: {}'.format(left_side))
        #print('This is the  right before recursion: {}'.format(right_side))
        #Recursive call
       
        #print ('Array before the recursion: {}'.format(array))
        
        merge_sort(left_side)
        merge_sort(right_side)

        #print('*******This is the left side after recursion : {}'.format(left_side))
        #print('*******This is the right side after recursion: {}'.format(right_side))
        #print ('********************Array after the recursion: {}'.format(array))


        #Iterators to cycle through the subarray
        i = 0
        j = 0
        #iterator for the main array
        k = 0

        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                array[k] = left_side[i]
                i += 1
            else:
                array[k] = right_side[j]
                j += 1
            
            k += 1

        #print(i, j, k)

        while  i < len(left_side):
            array[k] = left_side[i]
            i += 1
            k += 1

        while j < len(right_side):
            array[k] = right_side[j]
            j += 1
            k += 1 
            
    return array


def run():
    array_size = int(input('Size of the array: '))
    array_to_sort = [random.randint(0, array_size) for i in range(array_size)]
    #print(array_to_sort)
    array_to_sort_2 = copy.deepcopy(array_to_sort)
    array_to_sort_3 = copy.deepcopy(array_to_sort)
    sorted_array = bubble_sort(array_to_sort)
    #print(sorted_array)
    sorted_insertion_array = insertion_Sort(array_to_sort_2)
    print(sorted_insertion_array)
    ini_time = time.time()
    sorted_merge_array = merge_sort(array_to_sort_3)
    fin_time = time.time()
    duration = fin_time - ini_time
    #print(sorted_merge_array)
    print('The algorithm isnertion sort took {} seconds to be executed'.format(duration))


if __name__ == "__main__":
    run()