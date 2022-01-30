# import randint function from random module
from random import randint
# import statistics module with arithmetic functions (to use mean function)
import statistics
# initialize an empty list named rand_list
rand_list = []
# define a variable for the number of list values. In our case it is 100.
n = 100
# define a variable for the minimum value of the list. In our case it is 0.
min_v = 0
# define a variable for the maximum value of the list. In our case it is 1000.
max_v = 1000

# In the try block, we execute the statement that might throw an exception, and in the except block, we catch them.
try:
    # define a cycle to generate the list
    for i in range(n):
        # add a new random element(number) to the list
        rand_list.append(randint(min_v, max_v))
# in the except block, we catch them (to avoid a crash)
except:
    # display a message if some error occurs
    print('\nError 1 occurs. Random list creation step.')

# rand_list display processing
try:
    print(f'\nList of {n} random numbers from {min_v} to {max_v}:  {rand_list}')
except:
    print('\nError 2 occurs. Random list printing step.')

# Sort the rand_list
# In the try block, we execute the statement
try:
    # Outer loop.
    # Create a cycle equal to the length of our list minus 1,
    # because the last number in the list has no neighbor on the right,
    # and therefore this comparison operation does not need to be performed.
    for i in range(n-1):
        # Inner loop, n-i-1 passes.
        # The number of iterations of the inner loop depends on the iteration number of the outer loop,
        # since the end of the list is already sorted, and it makes no sense in iterating through these elements.
        # As a result of one pass of the inner loop, the largest element is placed at the end of the list,
        # and the smallest element is moved one position closer to the beginning.
        for j in range(n-i-1):
            # Compare the current element ([j]) with the next ([j+1]).
            if rand_list[j] > rand_list[j+1]:
                # If the current element is greater than the next, swap them.
                # It can be done using multiple assignment.
                # It allows not to introduce an additional temporary variable to swap the values of two elements.
                rand_list[j], rand_list[j+1] = rand_list[j+1], rand_list[j]
# in the except block to catch them if some kind of error happened (to avoid a crash)
except:
    print('\nError 3 occurs. Sorting rand_list step.')

# Sorted rand_list display processing
try:
    print(f'\nSorted numbers:  {rand_list}')
except:
    print('\nError 4 occurs. Sorted numbers printing step.')

# initialize an empty list named even_list
even_list = []
# initialize an empty list named odd_list
odd_list = []
try:
    # take each element (number) of rand_list in turn
    for i in rand_list:
        # if there is no remainder of division when divided by 2
        if not i % 2:
            # add a new element (number) to the list of even numbers
            even_list.append(i)
        # if there is a remainder of division when divided by 2.
        else:
            # add a new element (number) to the list of odd numbers
            odd_list.append(i)
except:
    print('\nError 5 occurs. Even_list, odd_list creation step.')

# even_list display processing
try:
    print(f'\nEven numbers:  {even_list}')
except:
    print('\nError 6 occurs. Even_list printing step.')

# odd_list display processing
try:
    print(f'\nOdd numbers:  {odd_list}')
except:
    print('\nError 7 occurs. Odd_list printing step.')

# Calculate the arithmetic mean of the even_list elements.
try:
    # To avoid division by zero, check if the number of elements in even_list is 0, then the result is 0 (avg_even = 0)
    avg_even = statistics.mean(even_list) if len(even_list) != 0 else 0
except:
    print('\nError 8 occurs. AVG calculation for even numbers step.')

# Calculate the arithmetic mean of the odd_list elements.
try:
    # To avoid division by zero, check if the number of elements in odd_list is 0, then the result is 0 (avg_odd = 0)
    avg_odd = statistics.mean(odd_list) if len(odd_list) != 0 else 0
except:
    print('\nError 9 occurs. AVG calculation for odd numbers step.')

# avg_even variable display processing
try:
    print(f'\nAVG of even numbers:  {avg_even}')
except:
    print('\nError 10 occurs. AVG of even numbers printing step.')

# avg_odd variable display processing
try:
    print(f'\nAVG of odd numbers:  {avg_odd}')
except:
    print('\nError 11 occurs. AVG of odd numbers printing step.')