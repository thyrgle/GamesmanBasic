DWULT = {
    'DRAW': 'D',
    'WIN': 'W',
    'UNDECIDED': 'U',
    'LOSS': 'L',
    'TIE': 'T'
}

def solve(primitive, do_move, gen_moves, initial_position):
    memo = {}

    def solve_position(cur_pos):
        ### Comment this out to test without memoizing ###
        if cur_pos in memo:
            return memo[cur_pos]
        ########
        result = primitive(cur_pos)
        if result == DWULT['UNDECIDED']:
            moves = gen_moves(cur_pos)
            new_positions = [do_move(cur_pos, move) for move in moves]
            losing_children = [pos for pos in new_positions if solve_position(pos) == DWULT['LOSS']]
            # ties and draws not handled yet
            result = DWULT['WIN'] if len(losing_children) else DWULT['LOSS']
        ### Comment this out to test without memoizing ###
        memo[cur_pos] = result
        ########
        return result

    return solve_position(initial_position())
