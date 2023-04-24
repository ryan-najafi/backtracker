from backtracker import backtracker as bt


def test_backtracker_subsets():
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
    assert get_subsets.output == [[], ['d'], ['c'], ['c', 'd'], ['b'], ['b', 'd'], ['b', 'c'], ['b', 'c', 'd']]
    
test_backtracker_subsets()