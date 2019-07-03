import numpy as np


def generate_frame(num_datapoints, size_side, thickness):
    """
    Generates a square with specified num_datapoints and size_side, cenetered at the origin

    :param int num_datapoints: number of datapoints that constitute the square
    :param int size_side: length of the side of the square
    :param float thickness: the size of the region across which the points are uniformly distributed
    :return: - x axis values (numpy array), and
             - y axis values (numpy array)
            of the datapoints constituting the square
    """
    num_side = num_datapoints // 4

    avgline = np.linspace(-size_side / 2, size_side / 2, num=num_side)
    lower_window = np.random.uniform(low=-thickness / 2., high=thickness / 2., size=int(num_side)) - size_side / 2.
    upper_window = np.random.uniform(low=-thickness / 2., high=thickness / 2., size=int(num_side)) + size_side / 2.

    x = np.concatenate((np.tile(avgline, 2), lower_window, upper_window))
    y = np.concatenate((lower_window, upper_window, np.tile(avgline, 2)))

    return x, y
