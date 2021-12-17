"""
Problem 15.Lattice paths
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly
6 routes to the bottom right corner. How many such routes are there through a 20×20 grid?
"""
from time_check import timer


@timer
def find_routes_amount(greed_size):
    array_size = greed_size+1
    array = [[0]*array_size for _ in range(array_size)]
    for i in range(array_size):
        for j in range(i, array_size):
            if i == 0 or j == 0:
                array[i][j] = 1
            elif i == j:
                array[i][j] = array[i-1][j]*2
            else:
                array[i][j] = array[i-1][j] + array[i][j-1]
    return array[greed_size][greed_size]


if __name__ == "__main__":
    find_routes_amount(20)
