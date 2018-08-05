def find_reverse(numbers):
    #TODO: find the reverse of the list
    numbers.reverse()
    return numbers

def find_max(numbers):
    #TODO: find the maximum of the list
    return max(numbers)

def find_min(numbers):
    #TODO: find the minimum of the list
    return min(numbers)

def find_sum(numbers):
    #TODO: find the sum of all the numbers in the list
    return sum(numbers)

def find_average(numbers):
    #TODO: find the average of all the numbers in the list
    average = sum(numbers)/len(numbers)
    return average

def find_descending(numbers):
    #TODO: numbers sorted in descending order
    numbers.sort(reverse=True)
    return numbers

def second_smallest(numbers):
    #TODO: find the second smallest

    smallest = list(set(numbers))
    return sorted(smallest)[1]
   
    '''num1, num2 = float("inf"), float("inf")
    for i in numbers:
        if i < num1:
            num1, num2 = i, num1
        elif i < num2:
            i = num2
    return num2'''

'''
 bonus task:
 a function that takes in a list of numbers, and an index 'k' 
 and prints the kth smallest number in the list
'''
def kth_smallest(numbers, k):
    #TODO: find the kth smallest number in the list
    smallest = list(set(numbers))
    return sorted(smallest)[k - 1]
