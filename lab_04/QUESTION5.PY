def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

if r > n:
    print("r should be less than or equal to n.")
else:
    nCr = factorial(n) / (factorial(r) * factorial(n - r))
    print(f"The value of {n}C{r} is: {nCr}")
