number = input("Enter a number: ")
length = len(number)

sum_of_powers = sum(int(digit) ** (index + 1) for index, digit in enumerate(number))

if sum_of_powers == int(number):
    print(f"{number} is a Disarium number.")
else:
    print(f"{number} is not a Disarium number.")
