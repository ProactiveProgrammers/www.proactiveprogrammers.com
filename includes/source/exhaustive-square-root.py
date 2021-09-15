x = 25
epsilon = 0.01
step = epsilon**2
num_guesses = 0
answer = 0.0
while abs(answer**2 - x) >= epsilon and answer <= x:
    answer += step
    num_guesses += 1
print(f"Guessed {num_guesses} times")
if abs(answer**2 - x) >= epsilon:
    print(f"Could not find square root of {x}")
else:
    print(f"{answer} is close to the square root of {x}")
