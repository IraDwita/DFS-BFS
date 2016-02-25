
############################################################
# Imports
############################################################

import math
import random
import copy

############################################################
# Section 1: N-Queens
############################################################

def num_placements_all(n):
    return math.factorial(n * n) / (math.factorial(n * n - n) * math.factorial(n))

def num_placements_one_per_row(n):
    return n ** n

def n_queens_valid(board):
    for (i, col_i) in enumerate(board):
        for (j, col_j) in enumerate(board):
            if i != j:
                if col_i == col_j:
                    return False
                if (col_i - col_j) == (i - j):
                    return False
                if (col_i - col_j) == (j - i):
                    return False
    return True

def n_queens_solutions(n):
'''solution to n-queens problem'''
    board = []
    frontier = [board]
    while True:
        if frontier == []:  # no element left in frontier
            return
        node = frontier.pop()   # pop out the last element, LIFO, DFS
        for i in range(n - 1, -1, -1):
            new_board = node + [i]
            if n_queens_valid(new_board):   # check valid first, if not, discard
                if len(new_board) == n:
                    yield new_board
                else:
                    frontier.append(new_board)

'''
# recursive version of n-queens solution
def n_queens_helper(n, board):
    if len(board) == n:
        nq_fanghan.append(board)
    else:
        for i in range(n):
            if n_queens_valid(board + [i]):
                n_queens_helper(n, board + [i])

def n_queens_solutions(n):
    global nq_fanghan
    nq_fanghan = []
    n_queens_helper(n, [])
    solu = (elem for elem in nq_fanghan)
    return solu
'''

############################################################
# Section 2: Lights Out
############################################################

class LightsOutPuzzle(object):

    def __init__(self, board):
        self.state = board
        self.row = len(board)
        if self.row == 0:
            self.col = 0
        else:
            self.col = len(board[0])

    def get_board(self):
        return self.state

    def perform_move(self, row, col):
        if row < 0 or row >= self.row or col < 0 or col >= self.col:
            return
        for (i, j) in ((row, col), (row-1, col), (row+1, col), (row, col-1), (row, col+1)):
            if i >= 0 and i < self.row and j >=0 and j < self.col:
                if self.state[i][j]:
                    self.state[i][j] = False
                else:
                    self.state[i][j] = True

    def scramble(self):
        for i in range(self.row):
            for j in range(self.col):
                if random.random() > 0.5:
                    self.perform_move(i, j)

    def is_solved(self):
        for i in range(self.row):
            for j in range(self.col):
                if self.state[i][j]:
                    return False
        return True

    def copy(self):
        return LightsOutPuzzle(copy.deepcopy(self.state))

    def successors(self):
        for i in range(self.row):
            for j in range(self.col):
                p = self.copy()
                p.perform_move(i, j)
                yield (i, j), p
    
    '''# First-row Search
    def find_solution(self):
        steps = float("inf")
        solution = []
        for times in range(2 ** self.col - 1, -1, -1):  # traverse all the situation of the first row
            p = self.copy()
            for bit in range(self.col - 1, -1, -1):     # traverse all the elements of the first row
                if (times & (2 ** bit)) >> bit:         # judge the bit of bin(times) is 1 or not
                    p.perform_move(0, self.col - 1 - bit)
            if judge_final_line(p, self.row, self.col): # if this is a solution
                steps_temp = 0
                solution_temp = []
                p = self.copy()
                for bit in range(self.col - 1, -1, -1):
                    if (times & (2 ** bit)) >> bit:
                        p.perform_move(0, self.col - 1 - bit)
                        steps_temp += 1
                        solution_temp.append((0, self.col - 1 - bit))
                for ii in range(1, self.row):
                    for jj in range(self.col):
                        if p.state[ii - 1][jj]:
                            p.perform_move(ii, jj)
                            steps_temp += 1
                            solution_temp.append((ii, jj))
                if steps_temp < steps:
                    steps = steps_temp
                    solution = solution_temp
        if solution == []:
            return None
        else:
            return solution
    '''

    def find_solution(self):
    '''solution to Lights Out Puzzle'''
        trace = {}  # store the board and the corresponding move to its parent
        solution = []
        if self.is_solved():
            return solution
        frontier = [self]   # add initial state
        while True:
            if frontier == []:      # no solution
                return None
            
            node = frontier.pop(0)  # pop the first element, FIFO, BFS
            
            for move, new_node in node.successors():    # generate children one by one
                board = tuple(tuple(x) for x in new_node.state)
                if board in trace:
                    continue
                else:
                    trace[board] = [move]

                if new_node.is_solved():    # find solution
                    while new_node.state != self.state:
                        check_board = tuple(tuple(x) for x in new_node.state)
                        solution = trace[check_board] + solution
                        new_node.perform_move(solution[0][0], solution[0][1])
                    return solution
                
                frontier.append(new_node)   # add new node to frontier only after testing

'''# a more powerful algorithm for solution to light out puzzle
def judge_final_line(p, row, col):
    for i in range(1, row):
        for j in range(col):
            if p.state[i - 1][j]:
                p.perform_move(i, j)
    for k in range(col):
        if p.state[row - 1][k]:
            return False
    return True
'''

def create_puzzle(rows, cols):
    board = []
    for i in range(rows):
        board += [[False] * cols]
    return LightsOutPuzzle(board)

############################################################
# Section 3: Linear Disk Movement
############################################################

class solve_disks(object):
    def __init__(self, length, n, grid):    # usually grid = 0 or [] when initialzing
        self.length = length
        self.n = n
        if grid == 0 or len(grid) == 0:
            self.grid = range(n) + [-1] * (length - n)
        elif len(grid) == length:
            self.grid = grid
        else:
            return

    def move(self, i, steps):
        if (i + steps) < 0 or (i + steps) >= self.length:
            return
        self.grid[i + steps] = self.grid[i]     # steps = -2, -1, 1, 2
        self.grid[i] = -1

    def is_identical_solved(self):
        for i in range(self.length - self.n):
            if self.grid[i] != -1:
                return False
        return True

    def is_distinct_solved(self):
        for i in range(self.length - self.n):
            if self.grid[i] != -1:
                return False
        for i in range(self.length - self.n, self.length):
            if self.grid[i] != self.length - i - 1:
                return False
        return True

    def copy(self):
        return solve_disks(copy.deepcopy(self.length), copy.deepcopy(self.n), copy.deepcopy(self.grid))

    def successors(self):
        for i in range(self.length):
            if (self.grid[i] != -1 and (i + 1) < self.length and self.grid[i + 1] == -1):
                d = self.copy()
                d.move(i, 1)
                yield (i, i + 1), d
                
            if (self.grid[i] != -1 and (i + 2) < self.length and self.grid[i + 1] != -1 and self.grid[i + 2] == -1):
                d = self.copy()
                d.move(i, 2)
                yield (i, i + 2), d
                
            if (self.grid[i] != -1 and (i - 1) >= 0 and self.grid[i - 1] == -1):
                d = self.copy()
                d.move(i, -1)
                yield (i, i - 1), d
                
            if (self.grid[i] != -1 and (i - 2) >= 0 and self.grid[i - 1] != -1 and self.grid[i - 2] == -1):
                d = self.copy()
                d.move(i, -2)
                yield (i, i - 2), d

def solve_identical_disks(length, n):
    disk = solve_disks(length, n, 0)
    trace = {}  # store the board and the corresponding move to its parent
    solution = []
    if disk.is_identical_solved():
        return solution
    frontier = [disk]   # add initial state
    while True:
        # no empty solution for this problem
        node = frontier.pop(0)  # FIFO
        
        for move, new_node in node.successors():    # generate children one by one
            grid = tuple(new_node.grid)
            if grid in trace:
                continue
            else:
                trace[grid] = [move]

            if new_node.is_identical_solved():    # find solution
                while new_node.grid != disk.grid:
                    check_grid = tuple(new_node.grid)
                    solution = trace[check_grid] + solution
                    new_node.move(solution[0][1], solution[0][0] - solution[0][1])
                return solution
            
            frontier.append(new_node)   # add new node to frontier only after testing

def solve_distinct_disks(length, n):
    disk = solve_disks(length, n, 0)
    trace = {}  # store the grid and the corresponding move to its parent
    solution = []
    if disk.is_distinct_solved():
        return solution
    frontier = [disk]   # add initial state
    while True:
        if frontier == []:
            return None
        
        node = frontier.pop(0)  # FIFO
        
        for move, new_node in node.successors():    # generate children one by one
            grid = tuple(new_node.grid)
            if grid in trace:
                continue
            else:
                trace[grid] = [move]

            if new_node.is_distinct_solved():    # find solution
                while new_node.grid != disk.grid:
                    check_grid = tuple(new_node.grid)
                    solution = trace[check_grid] + solution
                    new_node.move(solution[0][1], solution[0][0] - solution[0][1])
                return solution
            
            frontier.append(new_node)   # add new node to frontier only after testing

