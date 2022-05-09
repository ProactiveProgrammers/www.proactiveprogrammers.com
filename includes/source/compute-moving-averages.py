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


if __name__ == "__main__":
    # Reference:
    # https://docs.python.org/3/library/statistics.html
    # Reference:
    # Refer to Chapter 11 of Programming and Mathematical Thinking
    small_data = [1, 2, 3, 4, 4]
    window = 5
    print(f"Computing the moving average for a small list of values {small_data}\n")
    for smoothed_value in smooth(small_data, window):
        print(f"\tCurrent moving average of {window} values is {smoothed_value}")
    print()
