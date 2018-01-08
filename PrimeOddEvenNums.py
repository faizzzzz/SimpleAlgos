from time import perf_counter
import math

def oddEvenNums( start, stop, nums):
    # Generate a list of odd numbers within a specified range(inclusive)
    numArray = []
    temp = start

    if nums.lower() == "odd":
        if temp%2 == 0:
            temp += 1

    if nums.lower() == "even":
        if temp%2 == 1:
            temp += 1

    numArray.append(temp)

    while temp < stop-1:
        temp += 2
        numArray.append(temp)

    return numArray

numList = oddEvenNums(3, 11, nums="even")
