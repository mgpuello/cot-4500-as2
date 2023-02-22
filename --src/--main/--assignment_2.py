''' ==========================================
== Written by..: Manuel Puello            ====
== Date Written: Feb 19                   ====
== Purpose.....: cot-4500 / Assignment 2  ====
==============================================
'''

import numpy as np
from scipy.linalg import solve

# Question 1

def nevilles_method(x_points, y_points, x):
    matrix_dimension = len(x_points)
    matrix = np.zeros((matrix_dimension, matrix_dimension))

    for index, row in enumerate(matrix):
        row[0] = y_points[index]

    num_of_points = len(x_points)
    for i in range(1, num_of_points):
        for j in range(1, i + 1):
            first_multiplication = (x - x_points[i - j]) * matrix[i][j - 1]
            second_multiplication = (x - x_points[i]) * matrix[i - 1][j - 1]

            denominator = x_points[i] - x_points[i - j]

            coefficient = (first_multiplication - second_multiplication) / denominator

            matrix[i][j] = coefficient

    print(matrix[num_of_points - 1][num_of_points - 1])
    print("\n")

# Question 2

def newton_method_and_approx():
    point_x0 = 7.2
    point_x1 = 7.4
    point_x2 = 7.5
    point_x3 = 7.6
    f_x0 = 23.5492
    f_x1 = 25.3913
    f_x2 = 26.8224
    f_x3 = 27.4589
    divided_difference_1 = (f_x1 - f_x0) / (point_x1 - point_x0)
    divided_difference_2 = (f_x2 - f_x1) / (point_x2 - point_x1)
    divided_difference_3 = (f_x3 - f_x2) / (point_x3 - point_x2)
    _2nd_divided_difference_1 = (divided_difference_2 - divided_difference_1) / (point_x2 - point_x0)
    _2nd_divided_difference_2 = (divided_difference_3 - divided_difference_2) / (point_x3 - point_x1)
    _3rd_divided_difference = (_2nd_divided_difference_2 - _2nd_divided_difference_1) / (point_x3 - point_x0)
    divided_dif = [divided_difference_1, divided_difference_2, divided_difference_3]
    print(divided_dif)
    print("\n")

# Question 3

    approximating_x = 7.3
    final_approximation = f_x0 + divided_difference_1 * (approximating_x - point_x0) + _2nd_divided_difference_1 * (approximating_x - point_x1) * (approximating_x - point_x0) \
          + _3rd_divided_difference * (approximating_x - point_x2) * (approximating_x - point_x1) * (approximating_x - point_x0)
    print(final_approximation)
    print("\n")

# Question 4

def apply_div_dif(matrix: np.array):
    for i in range(2, len(matrix)):
        for j in range(2, i + 2):

            if j >= len(matrix[i]) or matrix[i][j] != 0:
                continue

            numerator = matrix[i][j - 1] - matrix[i - 1][j - 1]

            denominator = matrix[i][0] - matrix[i - j + 1][0]

            operation = numerator / denominator
            matrix[i][j] = operation
        
        return matrix

def hermite_interpolation():
    x_points = [3.6, 3.8, 3.9]
    y_points = [1.675, 1.436, 1.318]
    slopes = [-1.195, -1.188, -1.182]

    size = len(x_points)
    matrix = np.zeros((size * 2, size * 2))

    index = 0
    for x in range(0, size * 2, 2):
        matrix[x][0] = x_points[index]
        matrix[x + 1][0] = x_points[index]
        index += 1

    index = 0
    for y in range(0, size * 2, 2):
        matrix[y][1] = y_points[index]
        matrix[y + 1][1] = y_points[index]
        index += 1

    index = 0
    for x in range(1, size * 2 - 1, 2):
        matrix[x][2] = slopes[index]
        matrix[x + 1][2] = (y_points[index] - y_points[index - 2]) / (x_points[index] - x_points[index - 2])
        matrix[5][2] = -1.182
        index += 1


    complete_matrix = apply_div_dif(matrix)

    print(complete_matrix)
    print("\n")

# Question 5

def cubic_spline_matrix(x, y):
    size = len(x)
    matrix: np.array = np.zeros((size, size))
    matrix[0][0] = 1
    matrix[1][0] = x[1] - x[0]
    matrix[1][1] = 2 * ((x[1] - x[0]) + (x[2] - x[1]))
    matrix[1][2] = x[2] - x[1]
    matrix[2][1] = x[2] - x[1]
    matrix[2][2] = 2 * ((x[3] - x[2]) + (x[2] - x[1]))
    matrix[2][3] = x[3] - x[2]
    matrix[3][3] = 1
    print(matrix)
    print("\n")

    c_s_0 = 0
    c_s_1 = ((3 / (x[2] - x[1])) * (y[2] - y[1])) - ((3 / (x[1] - x[0])) * (y[1] - y[0]))
    c_s_2 = ((3 / (x[3] - x[2])) * (y[3] - y[2])) - ((3 / (x[2] - x[1])) * (y[2] - y[1]))
    c_s_3 = 0
    cubic_spline = np.array([c_s_0, c_s_1, c_s_2, c_s_3])
    print(cubic_spline)
    print("\n")

    f_x = [[matrix]]
    g_x = [[c_s_0], [c_s_1], [c_s_2], [c_s_3]]

    h_x = solve(f_x, g_x)

    print(h_x.T[0])
    print("\n")

if __name__ == "__main__":
    np.set_printoptions(precision=7, suppress=True, linewidth=100)

    # Nevilles_method
    x_points = [3.6, 3.8, 3.9]
    y_points = [1.675, 1.436, 1.318]
    approximated_x = 3.7
    nevilles_method(x_points, y_points, approximated_x)

    # Newton_approximation
    newton_method_and_approx()

    # Divided_method_approximation
    hermite_interpolation()

    # Cubic_spline
    x = [2, 5, 8, 10]
    y = [3, 5, 7, 9]
    cubic_spline_matrix(x, y)

