num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero)"

print(f"Addition: {addition:.2f}")
print(f"Subtraction: {subtraction:.2f}")
print(f"Multiplication: {multiplication:.2f}")
print(f"Division: {division}" if division == "Undefined (division by zero)" else f"Division: {division:.2f}")
