# backtracker
Generic implementation of a backtracker algorithm based on [Steven Skiena](https://www3.cs.stonybrook.edu/~algorith/video-lectures/2007/lecture15.pdf) in python.

# Usage

pip install backtracker==0.0.4

In Python:

from backtracker import backtracker as bt

a = []
k = 0
input = ['a', 'b', 'c', 'd']

def is_solution(a, k, input):
    return len(a) == len(input)

def process_solution(a, k, input, output, is_finished):
    result = []
    for i, c in enumerate(a):
        if c:
            result.append(input[i])
    if len(result) == 3:
        is_finished[0] = True
    output.append(result)

def get_candidates(a, k, input):
    return [False, True]

def make_move(a, k, input, c):
    a.append(c)

def unmake_move(a, k, input, c):
    a.pop()

get_subsets = bt.BackTracker(a, k, input, is_solution, process_solution, get_candidates, make_move, unmake_move)
get_subsets.back_track()
print(get_subsets.output)  
