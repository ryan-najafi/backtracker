# BackTracker Class
The BackTracker class is a Python implementation of the backtracking algorithm, designed for solving problems where a sequence of decisions leads to a solution. This generic framework can be adapted to various problems, such as puzzles, crosswords, combinatorial problems, etc.

This is based on [Steven Skiena](https://www3.cs.stonybrook.edu/~algorith/video-lectures/2007/lecture15.pdf).

GitHub Page: https://github.com/ryan-najafi/backtracker


## Features
Generic backtracking implementation.
Customizable for a wide range of problems.
Allows defining problem-specific solution processing, candidate generation, and move making/unmaking.

## Installation
pip install backtracker==0.0.7

## Usage
To use the BackTracker class, you need to define functions for:

Checking if a current state is a solution (is_solution).
Processing a complete solution (process_solution).
Generating candidate moves (get_candidates).
Making a move (make_move).
Unmaking a move (unmake_move).

Here's an example demonstrating how to use the BackTracker class to generate combinations of elements:

```
from backtracker import backtracker as bt

from backtracker import BackTracker

a = []
level = 0

def is_solution(a, k, input):
    return len(a) == len(input)

def process_solution(a, k, input):
    result = []
    for i, item in enumerate(a):
        if item:
            result.append(input[i])
    return ''.join(result)

def get_candidates(a, k, input):
    return [False, True]

def make_move(a, k, input, c):
    a.append(c)

def unmake_move(a, k, input, c):
    a.pop()

input = list('abc')
back_tracker = BackTracker(a=a, level=0, input=input, 
                           is_solution=is_solution, 
                           process_solution=process_solution, 
                           get_candidates=get_candidates, 
                           make_move=make_move, 
                           unmake_move=unmake_move)

for sol in back_tracker.get_next_solution():
    print(sol)
  
```


In this example, the BackTracker class is used to generate all combinations of the elements in the list 'abc'. The is_solution, process_solution, get_candidates, make_move, and unmake_move functions are defined to suit this specific problem.

## Contributing
Contributions to enhance BackTracker are welcome. Please adhere to the standard Python coding guidelines.

## License
This project is open-source and available under the MIT License.

