def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Example usage
numbers = [1, 2, 3, 4, 5]
print("Sum of list:", sum_of_list(numbers))
def sum_of_list1(numbers):
    return sum(numbers)

# Example usage
numbers = [1, 2, 3, 4, 5]
print("Sum of list:", sum_of_list1(numbers)) 