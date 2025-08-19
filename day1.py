import random
# imports random

#creates the array
testarray = ["a", "b", "c", "d", "e", "f", "g"]

# defines the function
def arraysearch(inputArray):
    # gets length of array
    arraylen = len(inputArray)
    #gets the index by using length of array [-1 for python because it starts at 0], the random value the array uses
    index = random.randint(0, arraylen-1)
    # returns the random value from the array
    return inputArray[index]

print(arraysearch(testarray))
