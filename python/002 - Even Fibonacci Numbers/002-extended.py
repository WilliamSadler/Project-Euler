import math
import timeit

"""I want to extend this function to any n, or at least make a faster version than in 002.py
As we approach far larger n's there is likely to be memory issues with the program, so will have to work that out at some point

For now however, I am just going to focus on getting the time complexity of the algorithm down
In my opinion, the best way to decrease this is to come up with a function that will give the nth Fibonacci number
E.g. nth Fibonacci number = Fib(n)

Luckily, there are Mathematicians that are far smarter than me that have come up with this function already, which includes the Golden Ratio
The formula is as follows:

         Phi^n - (-phi)^n
Fib(n) = —————————————————
           sqrt(5)

Where:         1 + sqrt(5)          1 - sqrt(5)
         Phi = —————————— and phi = ————————————
                   2                    2

Secondly we should take a look at the Fibonacci sequence, to see if there is any obvious pattern for which the even numbers occur:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, ...
^        ^        ^          ^            ^              ^               ^                  ^

It becomes obvious that the even Fibonacci numbers occur every 3 terms.
So we have found a nice pattern where we only need to consider the terms that are divisibly by three
(Assuming with 0 as the '0th' term and work up).
"""

def Fib(x):
    """Returns the xth Fiboacci number"""
    Phi = (1+math.sqrt(5))/2
    phi = (1-math.sqrt(5))/2

    return int(round((pow(Phi, x)-(pow(-phi, x)))/math.sqrt(5)))

def compute(n):
    i = 1
    even_sum = 0
    while True: #Messy lol, don't want to call fib function more than once
        fib_value = Fib(3*i)
        print(fib_value)
        if fib_value > n:
            return even_sum
        else:
            even_sum = even_sum + fib_value
            i=i+1

if __name__ == "__main__":

    n = int(input("Enter n: "))
    start = timeit.default_timer()
    print("Sum of even fib terms: %d" % compute(n))

    stop = timeit.default_timer()
    print('Time: ', stop - start)  

"""Using the timeit library I compared this method to the methods in 002.py (iterative and recursive)
The approximate runtime for this program, using our Fib(x) method the sum of even Fib terms under 4,000,000
was approximately 6.5 ms (milliseconds)
Compared to:
Iteratively: ~21ms (almost 3x slower)
Recursively: (not completed yet)

Even with lower numbers this method is far faster than when running the iterative functions,
I will possibly look into larger numbers in the future.
"""