# Run pytest to run these tests.
from backtracker import backtracker as bt


def test_backtracker_subsets():
    input = ['a', 'b', 'c']

    def is_solution(a, level, input):
        return len(a) == len(input)

    def process_solution(a, level, input):
        result = []
        for i, c in enumerate(a):
            if c:
              result.append(input[i])
        return ''.join(result)

    def get_candidates(a, level, input):
        if len(a) > len(input):
          return []
        else:
          return [False, True]

    def make_move(a, level, input, c):
        a.append(c)

    def unmake_move(a, level, input, c):
        a.pop()

    subsets = bt.BackTracker(input=input, 
                             is_solution=is_solution, 
                             process_solution=process_solution, 
                             get_candidates=get_candidates, 
                             make_move=make_move, 
                             unmake_move=unmake_move)
    assert sorted([x for x in subsets.solutions()]) == sorted(['', 'c', 'b', 'bc', 'a', 'ac', 'ab', 'abc'])

def test_backtracker_permutations():
    def is_solution(a, level, input):
        return len(a) == len(input)

    def process_solution(a, level, input):
        return ''.join(a)

    def get_candidates(a, level, input):
        return list(set(input) - set(a))

    def make_move(a, level, input, c):
        a.append(c)

    def unmake_move(a, level, input, c):
        a.pop()

    input = list('abc')
    permutations = bt.BackTracker(input=input, 
                            is_solution=is_solution, 
                            process_solution=process_solution, 
                            get_candidates=get_candidates, 
                            make_move=make_move, 
                            unmake_move=unmake_move)

    assert sorted([x for x in permutations.solutions()]) == sorted(['bac', 'bca', 'abc', 'acb', 'cba', 'cab'])


def test_backtracker_sudoku():
    input =  [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    def is_solution(a, level, input):
        return level == 9 * 9

    def process_solution(a, level, input):
        return input

    def get_candidates(a, level, input):
        row = level // 9
        col = level % 9
        if level >= 9*9:
            return []
        if input[row][col] !=0:
            return [input[row][col]]
        else:
            col_values = set([x[col] for x in input])
            rect_3x3 = []
            for i in range(3 * (row // 3), 3+3 * (row // 3)) :
                for j in range(3 * (col // 3),3 + 3 * (col // 3)):
                    rect_3x3.append(input[i][j])

            return list(set(list(range(1, 10))) - set(input[row]) - col_values - set(rect_3x3))

    def make_move(a, level, input, c):
        a.append(c)
        input[level // 9][level % 9] = c


    def unmake_move(a, level, input, c):
        a.pop()
        input[level // 9][level % 9] = 0


    sudoku_solver = bt.BackTracker(input=input, 
                             is_solution=is_solution, 
                             process_solution=process_solution, 
                             get_candidates=get_candidates, 
                             make_move=make_move, 
                             unmake_move=unmake_move)
    for x in sudoku_solver.solutions():
        sol = x
        break

    for row in sol:
        assert set(row) == set(list(range(1, 10)))
    for col in range(len(sol)):
        col_values = set([x[col] for x in sol])
        assert set(col_values) == set(list(range(1, 10)))

    for m in range(3):
        for n in range(3):
            rect_3x3 = []
            for i in range(3 * m, 3+3 * m) :
                for j in range(3 * n,3 + 3 * n):
                    rect_3x3.append(input[i][j])
            assert set(rect_3x3) == set(list(range(1, 10)))


test_backtracker_subsets()
test_backtracker_permutations()
test_backtracker_sudoku()