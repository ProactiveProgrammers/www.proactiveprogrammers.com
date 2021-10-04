def fibonacci_recursive(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

for i in range(10):
    print(f"fib of {i} is {fibonacci_recursive(i)}")
