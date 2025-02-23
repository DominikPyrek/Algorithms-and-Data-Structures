list_forbinary = [2*x for x in range(0,1000)]

def BinarySearch_iterative(list, target):
    startOfArray = 0
    endOfArray = len(list) - 1
    while startOfArray <= endOfArray:
        middleOfArray = startOfArray + (endOfArray - startOfArray) // 2
        if list[middleOfArray] == target:
            return middleOfArray
        elif list[middleOfArray] < target:
            startOfArray = middleOfArray + 1
        else:
            endOfArray = middleOfArray - 1
    return "Nie znaleziono takiej liczby"
            
print(BinarySearch_iterative(list_forbinary, 2))

def BinarySearch_recursive(list, target, startOfArray, endOfArray):
    if startOfArray > endOfArray:
        return "Nie znaleziono takiej liczby"
    middleOfArray = startOfArray + (endOfArray - startOfArray) // 2
    if list[middleOfArray] == target:
        return middleOfArray
    elif list[middleOfArray] < target:
        return BinarySearch_recursive(list, target, middleOfArray +1, endOfArray)
    else:
        return BinarySearch_recursive(list, target, startOfArray, middleOfArray - 1)

print(BinarySearch_recursive(list_forbinary, 2, 0, len(list_forbinary)))
