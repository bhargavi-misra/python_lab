number = int(input("Enter a number: "))
digit_sum = sum(int(digit) for digit in str(number))

if number % digit_sum == 0:
    print(f"{number} is a Harshad number.")
else:
    print(f"{number} is not a Harshad number.")
