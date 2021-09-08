def compute_square_while(value: int) -> int:
    """Compute the square of a number through iteration."""
    num_iterations = 0
    answer = 0
    while num_iterations < value:
        answer = answer + value
        num_iterations = num_iterations + 1
    return answer


def compute_square_for(value: int) -> int:
    """Compute the square of a number through iteration."""
    answer = 0
    for _ in range(abs(value)):
        answer = answer + abs(value)
    return answer


# computes the correct value
value = 3
value_squared = compute_square_while(value)
print()
print(f"The value of {value}*{value} is {value_squared}")

# does not compute the correct value
value = -3
value_squared = compute_square_while(value)
print()
print(f"The value of {value}*{value} is {value_squared}")
