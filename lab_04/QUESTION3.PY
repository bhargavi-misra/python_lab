for number in range(1, 1001):
    num_str = str(number)
    num_length = len(num_str)
    sum_of_powers = sum(int(digit) ** num_length for digit in num_str)

    if sum_of_powers == number:
        print(number)
