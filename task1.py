def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Taking input from the user
try:
    terms = int(input("Enter the number of terms in Fibonacci series: "))
    if terms <= 0:
        print("Please enter a positive integer.")
    else:
        result = fibonacci(terms)
        print("Fibonacci series:")
        print(result)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
