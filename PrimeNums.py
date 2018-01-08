from time import perf_counter
import math, numpy

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

    if number == 2 or number == 3 or number == 5:
        return number
    if number % 2 !=0:
        for divider in range(3, int(math.ceil(math.sqrt(number)) + 1), 2):
            # the number to be tested is divided by a range of numbers from starting from 2 to the square root of that
            # number.

            # n = a*b
            # If both a and b were greater than the square root of n, a*b would be greater than n. So at least one of
            # those factors must be less than or equal to the square root of n, and to check if n is prime, we only need
            #  to test for factors less than or equal to the square root.

            # print('The number is: ', number, " and The divider is: ", divider)
            remainder = number % divider
            if remainder == 0:
                isPrime = False
                # print("The number ", number, " is a not prime number")
                # If the remainder is 0, it means that the number is not prime. The for loop ends, and the loop moves on
                #  to the next number.
                break

            else:
                isPrime = True

    if isPrime:
        # print(number, " is a prime number")
        return number

def primeNumbersEffCheck(number, primeNums):
    isPrime = False
    # primeNums = numpy.ones((1), dtype=int) * 2
    # primeNums = numpy.delete(primeNums, (0), axis=0)
    if number == 2 or number == 3 or number == 5:
        # primeNums = numpy.append(primeNums, number)
        return number

    else:
        for divider in primeNums:
            if divider >= math.ceil(math.sqrt(number) + 1):
                break

            # print('The number is: ', number, " and The divider is: ", divider)
            remainder = number % divider
            if remainder == 0:
                isPrime = False
                break

            else:
                isPrime = True



    if isPrime == True:
       # primeNums = numpy.append(primeNums, number)
        return number

# return primeNums

def primeNumbersEff(start, stop):
    primeNums = []
    for number in range(start, stop):

        prime = primeNumbersEffCheck(number, primeNums)

        if prime is not None:
            primeNums.append(prime)

    return primeNums



def primeNumbers(start, stop):
    primeNums = []
    for number in range(start, stop):

        prime = primeCheck(number)

        if prime is not None:
            primeNums.append(prime)

    return primeNums



# numList = oddEvenNums(3, 11, nums="even")

wantPrint = False
wantBoth = True
start = 1
stop = 500000

# Method 1
print("method1: ")
t1 = perf_counter()
numList = primeNumbersEff(start, stop)
if wantPrint:
    for each in numList:
       print(each)
print(len(numList))
t2 = perf_counter()
meth1T = t2-t1
print(meth1T)

# Method 2
if wantBoth:
    print("\nmethod2: ")
    numList = primeNumbers(start, stop)
    if wantPrint:
        for each in numList:
           print(each)
    print(len(numList))
    t3 = perf_counter()
    meth2T = t3-t2
    print(meth2T, "\n")

    if meth1T > meth2T:
        print("Method 2 is ", (meth1T/meth2T), " times faster than method 1")
    if meth1T < meth2T:
        print("Method 1 is ", (meth2T/meth1T), " times faster than method 2")
