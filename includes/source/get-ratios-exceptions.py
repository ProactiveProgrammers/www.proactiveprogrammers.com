from typing import List

def get_ratios(one: List, two: List) -> List[float]:
    ratios = []
    for index in range(len(one)):
        try:
            ratios.append(one[index] / two[index])
        except ZeroDivisionError:
            ratios.append(float('nan'))
        except:
            raise ValueError("Incorrect arguments")
    return ratios

try:
    print(get_ratios([1, 2, 7, 6], [1, 2, 0, 3]))
    print(get_ratios([], []))
    print(get_ratios([1, 2, 7], [1, 2, 10, 3]))
    print(get_ratios([1, 2, 7, 6], [1, 2, 10]))
except ValueError as message:
    print(message)


print(get_ratios([1, 2, 7], [1, 2, 10, 3]))
print(get_ratios([1, 2, 7, 6], [1, 2, 10]))
