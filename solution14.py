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

def get_neighbor_sum(padded_grid, method):
    if method == 'indexing':
        return (
            padded_grid[:-2, :-2] +
            padded_grid[:-2, 1:-1] +
            padded_grid[:-2, 2:] +
            padded_grid[1:-1, :-2] +
            padded_grid[1:-1, 2:] +
            padded_grid[2:, :-2] +
            padded_grid[2:, 1:-1] +
            padded_grid[2:, 2:]
        )
    elif method == 'item':
        return (
            padded_grid[:-2, :-2].sum() +
            padded_grid[:-2, 1:-1].sum() +
            padded_grid[:-2, 2:].sum() +
            padded_grid[1:-1, :-2].sum() +
            padded_grid[1:-1, 2:].sum() +
            padded_grid[2:, :-2].sum() +
            padded_grid[2:, 1:-1].sum() +
            padded_grid[2:, 2:].sum()
        )
    elif method == 'flat':
        return (
            padded_grid[:-2, :-2].flat[0] +
            padded_grid[:-2, 1:-1].flat[0] +
            padded_grid[:-2, 2:].flat[0] +
            padded_grid[1:-1, :-2].flat[0] +
            padded_grid[1:-1, 2:].flat[0] +
            padded_grid[2:, :-2].flat[0] +
            padded_grid[2:, 1:-1].flat[0] +
            padded_grid[2:, 2:].flat[0]
        )

def update_grid_np(grid, method):
    new_grid = np.copy(grid)

    padded_grid = np.pad(grid, 1, mode='constant', constant_values=0)
    neighbors_count = get_neighbor_sum(padded_grid, method)

    new_grid[(grid == 0) & (neighbors_count == 3)] = 1
    new_grid[(grid == 1) & ((neighbors_count < 2) | (neighbors_count > 3))] = 0

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
simulate_np(initial_grid_np, ITERATIONS, 'flat')

#Simulation with list took 49.052925 seconds
#Simulation with NumPy (indexing) took 0.357805 seconds
#Simulation with NumPy (item) took 0.154006 seconds
#Simulation with NumPy (flat) took 0.169240 seconds