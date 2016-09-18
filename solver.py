WIN, LOSS, TIE, DRAW, UNDECIDED = 0, 1, 2, 3, 4


def solver(init_state, primitive, gen_moves, do_move):
    memo = {}

    def solve(cur_state):
        if cur_state in memo:
            return memo[cur_state]
        result = primitive(cur_state)
        if result == UNDECIDED:
            result = WIN if len([state for state in [do_move(cur_state, move) for move in gen_moves(cur_state)] if solve(state) == LOSS]) else LOSS
        memo[cur_state] = result
        return result

    return solve(init_state())