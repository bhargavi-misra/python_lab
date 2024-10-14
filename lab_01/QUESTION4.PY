num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

average = (num1 + num2) / 2
deviation1 = abs(num1 - average)
deviation2 = abs(num2 - average)

print(f"Average: {average:.2f}")
print(f"Deviation of the first number: {deviation1:.2f}")
print(f"Deviation of the second number: {deviation2:.2f}")
