
def determine_even_odd(value: int) -> str:
    """Determine if a number is even or odd."""
    if value % 2 == 0:
        return "even"
    else:
        return "odd"

number = 10
response = determine_even_odd(number)
print(f"The number of {number} is {response}!")

number = 11
response = determine_even_odd(number)
print(f"The number of {number} is {response}!")
