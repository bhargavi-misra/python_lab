numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers]
total_sum = sum(numbers)

print(f"The sum of the numbers is: {total_sum}")
