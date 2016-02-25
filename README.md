# DFS-BFS
N-queens for DFS, Light Out Puzzle for BFS, Linear Disk Movement for BFS


N-Queens: (DFS)

Representation: a sensible representation for a board configuration is a list of numbers between 00 and n−1n−1, 
where the iith number designates the column of the queen in row ii for 0≤i<n0≤i<n. A complete configuration is 
then specified by a list containing nn numbers.

The commond "n_queens_solutions(n)" (where n is a number such as 4, 5, 6, etc.) yields all valid placements of 
n queens on an n by n board, using the representation discussed above.

Eg. run following code and get corresponding results

    >>> solutions = n_queens_solutions(4)
    
    >>> next(solutions)
    
    [1, 3, 0, 2]
    
    >>> next(solutions)
    
    [2, 0, 3, 1]
    
    >>> list(n_queens_solutions(6))
    
    [[1, 3, 5, 0, 2, 4], [2, 5, 1, 4, 0, 3],
     [3, 0, 4, 1, 5, 2], [4, 2, 0, 5, 3, 1]]
     
    >>> len(list(n_queens_solutions(8)))
    
    92
    


Light Out Puzzle: (BFS)

The Lights Out puzzle consists of an m by n grid of lights, each of which has two states: on and off. The goal of 
the puzzle is to turn all the lights off, with the caveat that whenever a light is toggled, its neighbors above, 
below, to the left, and to the right will be toggled as well. If a light along the edge of the board is toggled, 
then fewer than four other lights will be affected, as the missing neighbors will be ignored.

You can play with an interactive version of the Lights Out puzzle using the provided GUI by running the following 
command:
python lights_out_gui.py rows cols
The arguments rows and cols are positive integers designating the size of the puzzle.

Eg. run in command line:

python lights_out_gui.py 3 3


Linear Disk Movement: (BFS)

The starting configuration of this puzzle is a row of l cells, with disks located on cells 0 through n−1. The goal 
is to move the disks to the end of the row using a constrained set of actions. At each step, a disk can only be moved 
to an adjacent empty cell, or to an empty cell two spaces away, provided another disk is located on the intervening 
square. Given these restrictions, it can be seen that in many cases, no movements will be possible for the majority 
of the disks. For example, from the starting position, the only two options are to move the last disk from cell n−1 
to cell n, or to move the second-to-last disk from cell n−2 to cell n.

Eg. run following code and get corresponding results

    >>> solve_distinct_disks(4, 2)
    
    [(0, 2), (2, 3), (1, 2)]
    
    >>> solve_distinct_disks(5, 2)
    
    [(0, 2), (1, 3), (2, 4)]
    
    >>> solve_distinct_disks(4, 3)
    
    [(1, 3), (0, 1), (2, 0), (3, 2), (1, 3), (0, 1)]
    
    >>> solve_distinct_disks(5, 3)
    
    [(1, 3), (2, 1), (0, 2), (2, 4), (1, 2)]
    

