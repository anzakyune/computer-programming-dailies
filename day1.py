import random

testarray = ["a", "b", "c", "d", "e", "f", "g"]

def arraysearch(inputArray):
    arraylen = len(inputArray)
    index = random.randint(0, arraylen-1)
    return inputArray[index]

print(arraysearch(testarray))
