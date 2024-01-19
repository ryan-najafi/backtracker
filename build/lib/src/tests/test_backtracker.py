from backtracker import backtracker as bt


def test_backtracker_subsets():
    a = []
    level = 0
    input = ['a', 'b', 'c']

    def is_solution(a, k, input):
        return len(a) == len(input)

    def process_solution(a, k, input):
        result = []
        for i, c in enumerate(a):
            if c:
              result.append(input[i])
        return ''.join(result)

    def get_candidates(a, k, input):
        return [False, True]

    def make_move(a, k, input, c):
        a.append(c)

    def unmake_move(a, k, input, c):
        a.pop()

    back_tracker = bt.BackTracker(a=a, level=0, input=input, is_solution=is_solution, process_solution=process_solution, get_candidates=get_candidates, make_move=make_move, unmake_move=unmake_move)
    assert [x for x in back_tracker.solutions()] == ['', 'c', 'b', 'bc', 'a', 'ac', 'ab', 'abc']


test_backtracker_subsets()