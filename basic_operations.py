'''Dynamic Sets Basic Operations'''

fruits = []

#Adding elementds to de list
fruits.append("Kiwi")
fruits.append("Berry")
fruits.append("Melon")
print(fruits)

#Pop removes the last element of the list
fruits.pop()
print(fruits)

#Adding Elements (The first value is the index)
fruits.insert(0,"Apple")
print(fruits)
fruits.insert(2,"Strawberry")
print(fruits)
#Using pop with an argument
fruits.pop(1)
print('Removing the element with index 1: \n')
print(fruits)
print('\n')
#Removing elements using the value
fruits.remove('Apple')
print('Using remove() to remove Apple: \n')
print(fruits)


def run():
    print('Building the Pyramid Sum')
    lower_limit = int(input("Instert the lower limit: "))
    upper_limit = int(input("Insert the upper limit: "))
    pyramid_sum(lower_limit, upper_limit)

def pyramid_sum(lower, upper, margin=0):
    
    blanks = " "* margin
    print(blanks, lower, upper)
    if lower > upper:
        print(blanks,0)
        return 0 
    else:
        result =  lower + pyramid_sum(lower + 1, upper, margin + 4)
        print(blanks, result)
        return result

if __name__=='__main__':
    run()