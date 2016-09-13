import solver
import fourtozero

num_calls = {}

"""
Helper to track how many times gen_moves is called for each pos.
If memoization is used, each position is expanded at most once.
"""
def gen_moves_track_memo(pos):
    if pos in num_calls:
        num_calls[pos] += 1
    else:
        num_calls[pos] = 0
    return fourtozero.gen_moves(pos)

def test_memoize():
    for _ in range(2):
        solver.solve(fourtozero.primitive, fourtozero.do_move, gen_moves_track_memo, fourtozero.initial_position)
        for pos in num_calls:
            assert num_calls[pos] <= 1
