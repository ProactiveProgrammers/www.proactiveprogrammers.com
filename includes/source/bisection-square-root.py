x = 25
epsilon = 0.01
step = epsilon**2
num_guesses = 0
low = 0
high = max(1,x)
answer = (high + low)/2
while abs(answer**2 - x) >= epsilon:
    num_guesses += 1
    if answer**2 < x:
        low = answer
    else:
        high = answer
    answer = (high + low)/2
print(f"Guessed {num_guesses} times")
if abs(answer**2 - x) >= epsilon:
    print(f"Could not find square root of {x}")
else:
    print(f"{answer} is close to the square root of {x}")
