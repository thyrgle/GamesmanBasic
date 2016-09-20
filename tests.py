import solver
import fourtozero

#test if solver has DWULT values
winning_numbers = [1, 2, 4]
losing_numbers = [0, 3]
#run the solver and make sure it outputs the correct W/L values


def has_WIN():
	for num in winning_numbers:
		assert solver.solver(num, fourtozero.primitive, fourtozero.gen_moves, fourtozero.do_moves) == fourtozero.WIN

def has_LOSE()):
	for num in losing_numbers:
		assert solver.solver(num, fourtozero.primitive, fourtozero.gen_moves, fourtozero.do_moves) == fourtozero.LOSE


#how do we test for DUT?
def has_DRAW():
	assert hasattr(solver, fourtozero.DRAW)

def has_UNDECIDED():
	assert hasattr(solver, fourtozero.UNDECIDED)

def has_TIE():
	assert hasattr(solver, fourtozero.TIE)



#test if solver satisfies the other GamesManAPI functions: do_moves, gen_moves, initial_position, primitive
def has_api_functions():
	assert callable(getattr(solver, "do_moves", None))
	assert callable(getattr(solver, "gen_moves", None))
	assert callable(getattr(solver, "initial_position", None))
	assert callable(getattr(solver, "primitive", None))
