## This program is meant to generate a matrix and find its LU decomposition using classic libraries

from random import *


def LU_initializer(matrix,size):
    l = []
    u = matrix.copy()  # initializing for u matrix

    for i in range(size):  # initializing for L matirx
        l.append([])
        for n in range(size):
            l[i].append(randint(1, 100))

    for j in range(size):  # filling basic entries for L matrix with zeros and ones
        for i in range(size):
            if (i <= j):
                u[i][j] = matrix[i][j]
                for k in range(i - 1):  # the pattern for
                    u[i][j] -= l[i][k] * u[k][j]
                if (i == j):
                    l[i][j] = 1
                else:
                    l[i][j] = 0

            else:  # the case with other entries in the matrix

                l[i][j] = matrix[i][j]
                for k in range(j):
                    l[i][j] -= l[i][k] * u[k][j]

                l[i][j] /= u[j][j]
                u[i][j] = 0

    return l,u


def main():

    matrix = []
    size = 5


    for i in range(size):  # create a list with nested lists
        matrix.append([])
        for n in range(size):
            matrix[i].append(randint(1, 100)) # fills nested lists with data

    print('generated matrix',matrix)
    l, u = LU_initializer(matrix,size)
    print('Matrix L is', l)
    print('Matrix U is', u)



if __name__ == '__main__':
    main()
