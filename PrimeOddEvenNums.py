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

def primeCheck(number):
    isPrime = False

    if number == 2 or number == 3:
        return number
    if number%2!=0:
        for divider in range(3, int(math.ceil(math.sqrt(number)) + 1), 2):
            # the number to be tested is divided by a range of numbers from starting from 2 to the square root of that
            # number.

            # n = a*b
            # If both a and b were greater than the square root of n, a*b would be greater than n. So at least one of
            # those factors must be less than or equal to the square root of n, and to check if n is prime, we only need
            #  to test for factors less than or equal to the square root.

            remainder = number % divider
            if remainder == 0:
                isPrime = False
                # print("The number ", number, " is a not prime number")
                # If the remainder is 0, it means that the number is not prime. The for loop ends, and the loop moves on
                #  to the next number.
                break

            else:
                isPrime = True

    if isPrime == True:
        # print(number, " is a prime number")
        return number


def primeNumbers(start, stop):
    primeNums = []
    for number in range(start, stop):

        prime = primeCheck(number)

        if prime is not None:
            primeNums.append(prime)

    return primeNums



# numList = oddEvenNums(3, 11, nums="even")

t1 = perf_counter()
numList = primeNumbers(1, 500000)
for each in numList:
    print(each)
t2 = perf_counter()
print(t2-t1)

