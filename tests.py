import nose
import fourtozero
import fourtozeromodified
import solver
ORIGINAL_DWULT = solver.WIN, solver.LOSS, solver.TIE, solver.DRAW, \
                 solver.UNDECIDED


def fourtozero_losing_state():
    return 0

def fourtozero_losing_states():
    return [0, 3]

def fourtozero_winning_states():
    return [1, 2, 4]

def fourtozero_modified_losing_states():
    return [0, 4]

def fourtozero_modified_winning_states():
    return [1, 2, 3]

def test_init_pos():
    assert solver.solver(fourtozero_losing_state, fourtozero.primitive,
                         fourtozero.gen_moves,
                         fourtozero.do_move) == solver.LOSS

def change_dwult():
    solver.WIN = 9
    solver.LOSS = 8
    solver.TIE = 7
    solver.DRAW = 6


def restore_dwult():
    solver.WIN = ORIGINAL_DWULT[0]
    solver.LOSS = ORIGINAL_DWULT[1]
    solver.TIE = ORIGINAL_DWULT[2]
    solver.DRAW = ORIGINAL_DWULT[3]


@nose.with_setup(change_dwult, restore_dwult)
def test_dwult_abstraction():
    assert solver.solver(fourtozero.init_state, fourtozero.primitive,
                         fourtozero.gen_moves,
                         fourtozero.do_move) == solver.WIN

# Tests different values for original 4 to 0 game
def test_four_to_zero_values():
    for losing_state in fourtozero_losing_states():
        assert solver.solver(lambda : losing_state, fourtozero.primitive,
                         fourtozero.gen_moves,
                         fourtozero.do_move) == solver.LOSS
    for winning_state in fourtozero_winning_states():
        assert solver.solver(lambda : winning_state, fourtozero.primitive,
                         fourtozero.gen_moves,
                         fourtozero.do_move) == solver.WIN

# Tests a different game: 4 to 0 where you can take 3 at a time
def test_four_to_zero_modified_values():
    for losing_state in fourtozero_modified_losing_states():
        assert solver.solver(lambda : losing_state, fourtozeromodified.primitive,
                         fourtozeromodified.gen_moves,
                         fourtozeromodified.do_move) == solver.LOSS
    for winning_state in fourtozero_modified_winning_states():
        assert solver.solver(lambda : winning_state, fourtozeromodified.primitive,
                         fourtozeromodified.gen_moves,
                         fourtozeromodified.do_move) == solver.WIN



        