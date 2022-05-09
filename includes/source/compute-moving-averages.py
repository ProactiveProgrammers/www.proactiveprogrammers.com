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
        else:
            return None


def smooth(data, num_points):
    average = MovingAverage(num_points)
    for value in data:
        average.append(value)
        yield average.value()


if __name__ == "__main__":
    data = [1, 2, 3, 4, 4]
    for smoothed_value in smooth(data, 5):
        print(smoothed_value)
