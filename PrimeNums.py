######################################################################################################################################
# Calculating prime numbers withinh a given range, using two different methods.
# Method 1 divides each number in the range by an odd number to check for prime.
# Method 2 stores the prime nums in an array and divides each number from that array. It only generates prime nums upto a number.
######################################################################################################################################

from time import perf_counter
import math, numpy

wantPrint = False   # print out the results or not. (Not recommended for large ranges.)
wantMethod = (1,1)  # this is to indicate which method to use. First argument is for method 1 and the second argument is for method 2.
start = 1           # lower limit of prime numbers.
stop = 500000       # upper limit of prime numbers.



# Method 1: Using odd numbers.

# This function checks for each number that is passed into it.
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

# Method 2: Using prime numbers.

# This function check each number that is passed into it. It does by dividing the number by the prime numbers in the 'primeNums' array.
def primeEffCheck(number, primeNums):
    isPrime = False         # Checks to see if the prime number is false or not.
    if number == 2 or number == 3 or number == 5:   # as these are known prime numbers, they are returned back and appended to the
        return number                               # primeNums array.

    else:
        for divider in primeNums:
            if divider >= math.ceil(math.sqrt(number) + 1):
                break       # If the divider is greater than the square root of the number(divisor) then the for loop ends.

            # print('The number is: ', number, " and The divider is: ", divider)
            remainder = number % divider    # remainder is calculated to check for prime.
            if remainder == 0:
                isPrime = False             # If the remainder is 0, the number is not a prime number, and the for loop ends.
                break

            else:
                isPrime = True              

    if isPrime == True:
        return number       # If the number is prime, it is returned.

def primeNumbers(start, stop, method):
    primeNums = []          # initializes the prime number array.
    for number in range(start, stop):
        if method == 1:                     # Calls the method 1 prime check for each number in the range
            prime = primeCheck(number)      # defined by the user.
        
        if method ==2 :
            prime = primeEffCheck(number, primeNums)        # Calls the method 2 prime check for each number in the range
                                                            # defined by the user.
        if prime is not None:                               
            primeNums.append(prime)     # The prime check methods might return a None value. If the value is not None, then it appends it
                                        # to the prime numbers array.
    return primeNums


# Method 1
if wantMethod == (1,0) or wantMethod == (1,1):
    t1 = perf_counter()     # saves the starting time.
    print("method1, Using odd numbers: ")
    numList = primeNumbers(start, stop, 1)      

    # prints the results.
    if wantPrint:
        for each in numList:
           print(each)

    print(len(numList))     # prints the number of prime numbers for comparison.
    t2 = perf_counter()     # saves the stopping time for method 1 and the starting time for method 2.
    meth1T = t2-t1          # subtracts both times to find the time taken for evaluation.
    print(meth1T)   

# Method 2
if wantMethod == (0,1) or wantMethod == (1,1):
    print("\nmethod2, Using prime numbers: ")
    numList = primeNumbers(start, stop, 2)
    
    # prints the results.
    if wantPrint:
        for each in numList:
           print(each)
    
    print(len(numList)) # pritns the number of prime numbers in the array for comparison.
    t3 = perf_counter() # saves the stopping time for method 2.
    meth2T = t3-t2      # subtracts both times to find the time taken for evaluation.
    print(meth2T, "\n")

# Evaluates which method is faster.
# If time for method 1 is greater, it means that method 2 is faster and vice versa.
if wantMethod == (1,1):
    if meth1T > meth2T:
        print("Method 2 is ", (meth1T/meth2T), " times faster than method 1")
    if meth1T < meth2T:
        print("Method 1 is ", (meth2T/meth1T), " times faster than method 2")
