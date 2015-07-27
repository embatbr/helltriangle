#!/usr/bin/python3.4


"""This is a module written solely to solve the Hell Triangle problem. The input
is written in the variable "example" (to avoid waste of time reading files or
user inputs), inside the code block "if __name__ == '__main__'" at the end of the
file.

TODO try 2 solutions: using lists and using NumPy.
"""


import random as rd


class InvalidNumLinesError(Exception):
    """Describes the errors occurred when the number of lines from a triangle is
    not a positive number.
    """

    def __init__(self, num_lines):
        if num_lines == 0:
            self.msg = 'The triangle must have at least 1 line.'
        elif num_lines < 0:
            self.msg = 'Negative number of lines? Really? Try again.'

    def __str__(self):
        return self.msg

class InvalidLimitsError(Exception):
    """Describes the errors occurred when the number of limits are not correct.
    """

    def __init__(self, limits):
        lim_min = limits[0]
        lim_max = limits[1]
        if lim_min == lim_max:
            self.msg = 'No variability of values.'
        elif lim_min > lim_max:
            self.msg = 'How can you have an interval starting from a point higher\
 than the end? Try again.'

    def __str__(self):
        return self.msg


def create_example(num_lines, limits):
    """Creates an example given the number of lines and the limits.
    """
    if num_lines < 1:
        raise InvalidNumLinesError(num_lines)

    lim_min = limits[0]
    lim_max = limits[1]
    if lim_min >= lim_max:
        raise InvalidLimitsError(limits)

    return [[rd.randint(lim_min, lim_max) for _ in range(i)] for i in range(1, num_lines + 1)]

def print_result(example, path, total):
    """Prints the maximum total in the form "X + Y + .... + Z = A".
    """
    print('path = %s' % path)
    print('total = %d' % total)
    if len(path) > 1:
        for pos in path[: -1]:
            print('%d + ' % example[pos[0]][pos[1]], end='')
    print('%d = %d' % (example[path[-1][0]][path[-1][1]], total))


def maximum_total(example, path=[(0, 0)], total=None):
    """Searches the "half matrix" for all paths and finds the better (higher sum).
    In case of a tie, the position "down" has preference over "downright".

    @param example: the triangle to be searched.
    @param path: the path that delivers the maximum total for a branch of example.
    @param total: the maximum total for a branch of example.

    @returns: a tuple containing path and total.
    """
    if len(path) == 1:
        total = example[0][0]
    if len(example) == 1:
        return (path, total)

    i = path[-1][0] + 1
    j = path[-1][1]
    j_right = j + 1

    path_down = path + [(i, j)]
    total_down = total + example[i][j]
    path_downright = path + [(i, j_right)]
    total_downright = total + example[i][j_right]

    if i < len(example) - 1:
        (path_down, total_down) = maximum_total(example, path_down, total_down)
        (path_downright, total_downright) = maximum_total(example, path_downright,
                                                          total_downright)

    if total_downright > total_down:
        return (path_downright, total_downright)
    else:
        return (path_down, total_down)


if __name__ == '__main__':
    import sys
    import time


    args = sys.argv[1 : ]

    num_lines = int(args[0])
    lim_min = int(args[1])
    lim_max = int(args[2])
    limits = (lim_min, lim_max)

    example = create_example(num_lines, limits)

    t = time.time()
    (path, result) = maximum_total(example)
    t = time.time() - t

    print('example = %s' % example)
    print_result(example, path, result)
    print('In %f microseconds' % (t*1e6))