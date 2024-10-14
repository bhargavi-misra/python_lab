num_terms = int(input("Enter the number of terms in the Fibonacci series: "))

a, b = 0, 1
fibonacci_series = []

for _ in range(num_terms):
    fibonacci_series.append(a)
    a, b = b, a + b

print("Fibonacci series:", fibonacci_series)
