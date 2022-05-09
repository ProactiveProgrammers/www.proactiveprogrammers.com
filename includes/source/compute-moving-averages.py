import random


class MovingAverage:

    def __init__(self, num_points):
        self.__points = []
        self.__length = 0
        self.__num_points = num_points

    def append(self, new_value):
        points = self.__points
        if self.__length == self.__num_points:
            points.pop(0)
        else:
            self.__length += 1
        points.append(new_value)

    def value(self):
        points = self.__points
        length = self.__length
        if length > 0:
            return sum(points) / length
        return None


def smooth(data, num_points):
    average = MovingAverage(num_points)
    for value in data:
        average.append(value)
        yield average.value()


def generate_random_integers(size, minimum, maximum):
    # Reference:
    # https://www.geeksforgeeks.org/generating-random-number-list-in-python/
    random_list = random.sample(range(minimum, maximum), size)
    return random_list


if __name__ == "__main__":
    # Reference:
    # https://docs.python.org/3/library/statistics.html
    # Reference:
    # Chapter 11 of Programminimumg and Mathematical Thinking
    # --> demonstrate the MovingAverage for a small fixed data set
    small_fixed_data = [1, 2, 3, 4, 4]
    window = 5
    print(f"Computing the moving average for a small, fixed list of values {small_fixed_data}\n")
    for smoothed_value in smooth(small_fixed_data, window):
        print(f"\tCurrent moving average of {window} values is {smoothed_value}")
    print()
    # --> demonstrate the MovingAverage for a small randomly generated data set
    small_random_data = generate_random_integers(5, 0, 100)
    window = 5
    print(f"Computing the moving average for a small, random list of values {small_random_data}\n")
    for smoothed_value in smooth(small_random_data, window):
        print(f"\tCurrent moving average of {window} values is {smoothed_value}")
    print()
    # --> demonstrate the MovingAverage for a medium randomly generated data set
    # --> define window to keep a small number of data values for the moving average
    small_random_data = generate_random_integers(50, 0, 100)
    window = 5
    print(f"Computing the moving average for a medium, random list of values {small_random_data}\n")
    for smoothed_value in smooth(small_random_data, window):
        print(f"\tCurrent moving average of {window} values is {smoothed_value:.4f}")
    print()
    # --> demonstrate the MovingAverage for a medium randomly generated data set
    # --> define window to keep a small number of data values for the moving average
    # --> make sure to use the same small_random_data set with the larger window
    window = 50
    print(f"Computing the moving average for a medium, random list of values {small_random_data}\n")
    for smoothed_value in smooth(small_random_data, window):
        print(f"\tCurrent moving average of {window} values is {smoothed_value:.4f}")
    print()
