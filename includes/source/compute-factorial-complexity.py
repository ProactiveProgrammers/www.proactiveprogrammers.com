def factorial(n: int) -> int:
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer

for i in range(10):
    print(f"factorial of {i} is {factorial(i)}")
