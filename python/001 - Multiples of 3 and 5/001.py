"""QUESTION:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000."""

"""SOLUTION EXPLAINATION:
The problem seems rather trivial at first, simply create some sort of loop to add up all multiples of 3s and then another to add up all multiples of 5s below 1000. However, some details should be considered.
We need to consider if there is any Double Counting going on in our logic, which is revealed to be the case when we consider numbers that are multiples of both 3 and 5, a.k.a multiples of 15 (3*5)
Therefore, when we come across a multiples of 15, we must take care either not to count them twice, or remove any double counting later on.

There are two obvious ways to approach the problem from here.
One would be to simply create a function that adds up the all the multiples of 3s and 5s below the given number (1000 in this case), then removing one sum of the set of the multiples of 15 under this number, which will recitfy and double counting that has occured.

The second, more favourable approach would be to use some simple mathematical forumla for the sum of all integers up to n, this being (1/2)*(n)*(n+1). 
If we wanted to the sum of the multiples of x up to n we can ammend this to a not so nice looking:
x*(1/2)*m*(m+1) where m = math.floor(n/x)
We can then construct some sort of equation using this formula to give sum(3)+sum(5)-sum(15) for the multiples of each number under n.
This will decrease the time complexity of our algorithm greatly, as we will only need to make a few calculations, rather than having to loop through all the multiples

To be honest, either option here is probably fine in the context of the given question, as we are only being asked for multiples up to 1000, but I'm going to write this program to just take any int n given, so might as well optimise to the best of my ability.
"""

import math

def compute(n):
    return sum_of_multiples(3,n) + sum_of_multiples(5,n) - sum_of_multiples(15, n)
    
def sum_of_multiples(x, n):
    """Finds the sum of the multiples of x below n"""
    m = math.floor(n/x)
    return int(x*(1/2)*m*(m+1))

if __name__ == "__main__":
    n = int(input("Enter n : "))
    print(compute(n-1)) #Subtract one as we are looking for the multiples less than n (not including)
