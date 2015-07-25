#!/usr/bin/python3.4


"""This is a lonely module, written solely to solve the Hell Triangle problem.
The input is written in the variable "example" (to avoid waste of time reading files
or user inputs),inside the code block "if __name__ == '__main__'" at the end of
the file.

TODO try 2 solutions: using lists and using NumPy.
TODO Use the "time" module (if that's it's real name) to check the execution time.
"""


def find_result(example, size, path, result):
    """In case of a tie, the pos "down" has preference over "downright".
    """
    i = path[-1][0] + 1
    j = path[-1][1]
    j_right = j + 1

    path_down = path + [(i, j)]
    result_down = result + example[i][j]
    path_downright = path + [(i, j_right)]
    result_downright = result + example[i][j_right]

    if i < size - 1:
        (path_down, result_down) = find_result(example, size, path_down, result_down)
        (path_downright, result_downright) = find_result(example, size, path_downright,
                                                         result_downright)

    if result_downright > result_down:
        return (path_downright, result_downright)
    else:
        return (path_down, result_down)


if __name__ == '__main__':
    example = [[6], [3, 5], [9, 7, 1], [4, 6, 8, 4]]
    (size, path, result) = (len(example), [(0, 0)], example[0][0])
    (path, result) = find_result(example, size, path, result)

    print(path)
    print(result)
    print('%d + ' % example[path[0][0]][path[0][1]], end='')
    for pos in path[1 : -1]:
        print('%d + ' % example[pos[0]][pos[1]], end='')
    print('%d = %d' % (example[path[-1][0]][path[-1][1]], result))