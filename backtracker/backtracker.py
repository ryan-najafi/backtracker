from typing import Any, Callable, List

class BackTracker():
    def __init__(
        self, 
        input: List[Any], 
        is_solution: Callable[[List[Any], int, List[Any]], bool], 
        process_solution: Callable[[List[Any], int, List[Any]], Any], 
        get_candidates: Callable[[List[Any], int, List[Any]], List[Any]], 
        make_move: Callable[[List[Any], int, List[Any], Any], None], 
        unmake_move: Callable[[List[Any], int, List[Any], Any], None],
        a: List[Any] = [], 
        level: int = 0,         
    ):
        '''
        Initializes the BackTracker class.

        Parameters:
        a (List[Any]): An array to hold the current partial solution.
        level (int): The current level in the backtracking process, initially set to the starting level.
        input (List[Any]): Problem-specific data required for solving the problem.
        is_solution (Callable): Function that checks if 'a' at the current level is a complete solution for the problem.
        process_solution (Callable): Function that processes a complete solution once found.
        get_candidates (Callable): Function that generates the next set of possible candidates for the solution.
        make_move (Callable): Function that updates 'a' with a new candidate.
        unmake_move (Callable): Function that reverts 'a' back to its state before the last move.
        '''
        self.a = a
        self.level = level
        self.input = input
        self.is_solution = is_solution
        self.process_solution = process_solution
        self.get_candidates = get_candidates
        self.make_move = make_move
        self.unmake_move = unmake_move

    def back_track(self) -> None:
        '''
        The main method for the backtracking algorithm. It recursively searches for a solution.

        The method checks if the current state of 'a' at the current level is a solution with 'is_solution'. If it is,
        the solution is processed using 'process_solution' and yielded. If not, the method
        generates new candidates and explores each recursively, making and unmaking moves as it progresses.
        '''    
        if self.is_solution(self.a, self.level, self.input):
            output = self.process_solution(self.a, self.level, self.input)
            yield output
        else:
            self.level += 1
            candidates = self.get_candidates(self.a, self.level, self.input)
            for c in candidates:
                self.make_move(self.a, self.level, self.input, c)
                yield from self.back_track()
                self.unmake_move(self.a, self.level, self.input, c)

    def solutions(self):
        '''
        Generator method to yield the next solution.

        Yields:
        The next solution found by the backtracking algorithm.
        '''
        yield from self.back_track()
        
if __name__ == "__main__":
    print("This is a class for backtracking problems.")
