import random
# imports random

#creates the array
testarray = ["a", "b", "c", "d", "e", "f", "g"]

# defines the function
def arraysearch(inputArray):
    arraylen = len(inputArray)  # gets length of array
    index = random.randint(0, arraylen-1) # random number from array length
    return inputArray[index]# returns the random value from the array

print(arraysearch(testarray)) # prints

