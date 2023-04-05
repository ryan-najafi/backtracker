class BackTracker():
  def __init__(self, a, k, input, is_solution, process_solution, get_candidates, make_move, unmake_move):
    self.a = a
    self.k = k
    self.input = input
    self.is_finished = False
    self.is_solution = is_solution
    self.process_solution = process_solution
    self.get_candidates = get_candidates
    self.make_move = make_move
    self.unmake_move = unmake_move
    self.output = []

  def back_track(self):
    if self.is_solution(self.a, self.k, self.input):
      self.process_solution(self.a, self.k, self.input, self.output)
    else:
      self.k += 1
      candidates = self.get_candidates(self.a, self.k, self.input)
      for c in candidates:
        self.make_move(self.a, self.k, self.input, c)
        self.back_track()
        self.unmake_move(self.a, self.k, self.input, c)
        if self.is_finished:
          return
