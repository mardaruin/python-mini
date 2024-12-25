import time
import numpy as np
import random
from copy import deepcopy

from socks import method


#working without numpy
def create_grid(size):
    return [[0 for _ in range(size)] for _ in range(size)]

def count_neighbors(grid, x, y):
    neighbors = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (i == x and j == y) or not (0 <= i < len(grid)) or not (0 <= j < len(grid)):
                continue
            neighbors += grid[i][j]
    return neighbors

def update_grid(grid):
    new_grid = deepcopy(grid)
    size = len(grid)
    for i in range(size):
        for j in range(size):
            neighbors = count_neighbors(grid, i, j)
            if grid[i][j]:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i][j] = 0
            else:
                if neighbors == 3:
                    new_grid[i][j] = 1
    return new_grid

def simulate(grid, iterations):
    start_time = time.time()
    current_grid = grid
    for _ in range(iterations):
        current_grid = update_grid(current_grid)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Simulation with list took {elapsed_time:.6f} seconds")
    return current_grid

#working with numpy
def create_grid_np(size):
    return np.zeros((size, size), dtype=np.uint8)

def get_neighbor_sum(grid, x, y, method):
    neighbors = 0

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (i == x and j == y) or not (0 <= i < len(grid)) or not (0 <= j < len(grid)):
                continue
            if method == 'indexing':
                neighbors += grid[i, j]
            elif method == 'item':
                neighbors += grid.item((i, j))
    return neighbors

def update_grid_np(grid, method):
    new_grid = np.copy(grid)
    size = len(grid)
    for i in range(size):
        for j in range(size):
            neighbors = get_neighbor_sum(grid, i, j, method)
            if method == 'indexing':
                if grid[i, j]:
                    if neighbors < 2 or neighbors > 3:
                        new_grid[i, j] = 0
                else:
                    if neighbors == 3:
                        new_grid[i, j] = 1
            elif method == 'item':
                if grid.item((i, j)):
                    if neighbors < 2 or neighbors > 3:
                        new_grid.itemset((i, j), 0)
                else:
                    if neighbors == 3:
                        new_grid.itemset((i, j), 1)
    return new_grid



def simulate_np(grid, iterations, method):
    start_time = time.time()
    current_grid = grid
    for _ in range(iterations):
        current_grid = update_grid_np(current_grid, method)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Simulation with NumPy ({method}) took {elapsed_time:.6f} seconds")
    return current_grid

#creating grid
SIZE = 1024
ITERATIONS = 12

initial_grid = create_grid(SIZE)
for i in range(SIZE):
    for j in range(SIZE):
        initial_grid[i][j] = random.randint(0, 1)

initial_grid_np = np.array(initial_grid)

simulate(initial_grid, ITERATIONS)
simulate_np(initial_grid_np, ITERATIONS, 'indexing')
simulate_np(initial_grid_np, ITERATIONS, 'item')