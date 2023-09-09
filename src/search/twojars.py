import search
import random
from random import randint
import util

# Module Classes


class TwoJarsState:
	"""
	This class represents a configuration of the two jars.
	"""

	def __init__(self, capacitys):
		"""
		  Constructs a new configuration.

		The configuration of the two jars is stored in a 2-tuple. 
		 - The first position stores the amount of water in the first jar (with capacity 4l).
		 - The second position stores the amount of water in the second jar (with capacity 3l).

		Both jars ware initially empty.
		"""
		self.jars = (capacitys[0], capacitys[1])
		self.max_capacity = [4, 3]

	def isGoal(self):
		"""
		  Checks to see if the pair of jars is in its goal state.

										---------
										| 2 | * |
										---------

		>>> TwoJarsState((2, 1)).isGoal()
		True

		>>> TwoJarsState((2, 0)).isGoal()
		True

		>>> TwoJarsState((1, 0)).isGoal()
		False
		"""
		"*** YOUR CODE HERE ***"
		return True if self.jars[0] == 2 else False
		util.raiseNotDefined()

	def legalMoves(self):
		"""
		  Returns a list of legal actions from the current state.

		Actions consist of the following:
		- fillJ3 (encher J3)
		- fillJ4 (encher J4)
		- pourJ3intoJ4 (despejar J3 em J4)
		- pourJ4intoJ3 (despejar J4 em J3)
		- emptyJ3 (esvaziar J3)
		- emptyJ4 (esvaziar J4)

		These are encoded as strings: 'fillJ3', 'fillJ4', 
		'pourJ3intoJ4', 'pourJ4intoJ3', 'emptyJ3', 'emptyJ4'.

		>>> TwoJarsState((1, 3)).legalMoves()
		['fillJ4', 'pourJ3intoJ4', 'emptyJ3', 'emptyJ4']
		"*** YOUR CODE HERE ***"
		"""

		legalActions = []
		j4, j3 = self.jars

		if j4 == 0:
				legalActions.extend(["fillJ4"])
		elif j4 == self.max_capacity[0]:
				legalActions.extend(["pourJ4intoJ3", "emptyJ4"])
		else:
				legalActions.extend(["fillJ4", "pourJ4intoJ3", "emptyJ4"])


		if j3 == 0:
				legalActions.extend(["fillJ3"])
		elif j3 == self.max_capacity[1]:
				legalActions.extend(["pourJ3intoJ4", "emptyJ3"])
		else:
				legalActions.extend(["fillJ3", "pourJ3intoJ4", "emptyJ3"])

		return legalActions
		util.raiseNotDefined()

	def legalMoves2(self):
		"""
		  Returns a list of legal actions from the current state.

		Actions consist of the following:
		- fillJ3 (encher J3)
		- fillJ4 (encher J4)
		- pourJ3intoJ4 (despejar J3 em J4)
		- pourJ4intoJ3 (despejar J4 em J3)
		- emptyJ3 (esvaziar J3)
		- emptyJ4 (esvaziar J4)

		These are encoded as strings: 'fillJ3', 'fillJ4', 
		'pourJ3intoJ4', 'pourJ4intoJ3', 'emptyJ3', 'emptyJ4'.

		>>> TwoJarsState((1, 3)).legalMoves()
		['fillJ4', 'pourJ3intoJ4', 'emptyJ3', 'emptyJ4']
		"*** YOUR CODE HERE ***"

		legalActions = []
		j4, j3 = self.jars

		if j4 == 0:
				legalActions.extend(["fillJ4"])
		elif j4 == self.max_capacity[0]:
				legalActions.extend(["pourJ4intoJ3", "emptyJ4"])
		else:
				legalActions.extend(["fillJ4", "pourJ4intoJ3", "emptyJ4"])


		if j3 == 0:
				legalActions.extend(["fillJ3"])
		elif j3 == self.max_capacity[1]:
				legalActions.extend(["pourJ3intoJ4", "emptyJ3"])
		else:
				legalActions.extend(["fillJ3", "pourJ3intoJ4", "emptyJ3"])

		return legalActions
		"""

		moves = []
		if self.jars[0] == 0:
			moves.append('fillJ4')
		if self.jars[1] == 0:
			moves.append('fillJ3')

		if self.jars[0] > 0 and self.jars[0] < 4:
			moves.append('fillJ4')
			moves.append('emptyJ4')

			if self.jars[1] < 3:
				moves.append('pourJ4intoJ3')

		if self.jars[1] > 0 and self.jars[1] < 3:
			moves.append('fillJ3')
			moves.append('emptyJ3')

			if self.jars[0] < 4:
				moves.append('pourJ3intoJ4')

		if self.jars[0] == 4:
			moves.append('emptyJ4')

			if self.jars[1] < 3:
				moves.append('pourJ4intoJ3')

		if self.jars[1] == 3:
			moves.append('emptyJ3')

			if self.jars[0] < 4:
				moves.append('pourJ3intoJ4')

		return moves

	def result(self, move):
		"""
		  Returns an object TwoJarsState with the current state based on the provided move.

		The move should be a string drawn from a list returned by legalMoves.
		Illegal moves will raise an exception, which may be an array bounds
		exception.

		NOTE: This function *does not* change the current object.  Instead,
		it returns a new object.
		"""
		"*** YOUR CODE HERE ***"

		# resultState = 0

		if move in ["emptyJ3", "emptyJ4"]:
			if move == "emptyJ3":
				# print("Esvaziar j3")
				resultState = TwoJarsState((self.jars[0], 0))
			else:
				# print("Esvaziar j4")
				resultState = TwoJarsState((0, self.jars[1]))

		elif move in ["pourJ3intoJ4", "pourJ4intoJ3"]:
			sum_vol = sum(self.jars)
			if move == "pourJ3intoJ4":
				# print(self.jars, min(sum_vol, self.max_capacity[0]))
				resultState = TwoJarsState(
					(min(sum_vol, self.max_capacity[0]), 0))
				# print("j4 <- j3")
			else:
				resultState = TwoJarsState(
					(0, min(sum_vol, self.max_capacity[1])))
				# print("j4 -> j3")

		else:
			if move in ["fillJ3", "fillJ4"]:
				if move == "fillJ3":
					resultState = TwoJarsState(
						(self.jars[0], self.max_capacity[1]))
					# print("Fill j3")
				else:
					# print(move)
					resultState = TwoJarsState(
						(self.max_capacity[0], self.jars[1]))
					# print("Fill j4")
			else:
				print("Erro, enhuma opção valida")
          
		return resultState
		util.raiseNotDefined()

	# Utilities for comparison and display
	def __eq__(self, other):
		"""
										Overloads '==' such that two pairs of jars with the same volume of water
		  are equal. ['fillJ4', 'pourJ4intoJ3', 'emptyJ4', 'fillJ3']

		  >>> TwoJarsState((0, 1)) == \
										  TwoJarsState((1, 0)).result('left')
		  True
		"""
		"*** YOUR CODE HERE ***"
		# print(other)
		return True if ((self.jars[0] == other.jars[0]) and (self.jars[1] == other.jars[1])) else False
		# util.raiseNotDefined()

	def __hash__(self):
		return hash(str(self.jars))

	def __getAsciiString(self):
		"""
		  Returns a display string for the maze
		"""
		"*** YOUR CODE HERE ***"
		return str(self.jars)

	def __str__(self):
		return self.__getAsciiString()


class TwoJarsSearchProblem(search.SearchProblem):
	"""
	  Implementation of a SearchProblem for the Two Jars domain

	  Each state is represented by an instance of an TwoJarsState.
	"""

	def __init__(self, start_state):
		"Creates a new TwoJarsSearchProblem which stores search information."
		self.start_state = start_state

	def getStartState(self):
		return self.start_state

	def isGoalState(self, state):
		return state.isGoal()

	def expand(self, state):
		"""
		  Returns list of (child, action, stepCost) pairs where
		  each child is either left, right, up, or down
		  from the original state and the cost is 1.0 for each
		"""
		child = []
		for a in self.getActions(state):
			next_state = self.getNextState(state, a)
			child.append(
				(next_state, a, self.getActionCost(state, a, next_state)))
		return child

	def getActions(self, state):
		return state.legalMoves()

	def getActionCost(self, state, action, next_state):
		assert next_state == state.result(action), (
			"getActionCost() called on incorrect next state.")
		return 1

	def getNextState(self, state, action):
		assert action in state.legalMoves(), (
			"getNextState() called on incorrect action")
		return state.result(action)

	def getCostOfActionSequence(self, actions):
		"""
		 actions: A list of actions to take

		This method returns the total cost of a particular sequence of actions.  The sequence must
		be composed of legal moves
		"""
		return len(actions)


def createRandomTwoJarsState(moves=10):
	"""
	  moves: number of random moves to apply

	  Creates a random state by applying a series 
	  of 'moves' random moves to a solved state.
	"""
	volume_of_J3 = randint(0, 4)

	a_state = TwoJarsState((0, volume_of_J3))

	for i in range(moves):
		# Execute a random legal move
		a_state = a_state.result(random.sample(a_state.legalMoves(), 1)[0])
	return a_state


def main():

	start_state = createRandomTwoJarsState(8)

	# a = TwoJarsState((1,0))
	# b = TwoJarsState((1,0))
	# c = TwoJarsState((0,1))

	# print(a == b, a == c, b == c)

	# for i in range(4):
	# 	for j in range(3):
	# 		start_state = TwoJarsState((i, j))
	# 		# Teste do legalMoves
	# 		# print(TwoJarsState((i, j)))
	# 		# print("Ações possiveis: ", sorted(start_state.legalMoves()))
	# 		# print("Ações possiveis: ", sorted(start_state.legalMoves2()), "\n")

	# 		# Teste das transições de estado (result)
	# 		for action in sorted(start_state.legalMoves2()):
	# 			print(start_state, action, start_state.result(action))
	# 		print()

	
 

			
	# return
	start_state = TwoJarsState((0, 0))
	print('A random initial state:', start_state)
	print("Ações possiveis: ", start_state.legalMoves())
	print("Ações possiveis: ", start_state.legalMoves2())

	# return
	problem = TwoJarsSearchProblem(start_state)
	path = search.breadthFirstSearch(problem)
	# print(path)

	print('BFS found a path of %d moves: %s' % (len(path), str(path)))

	curr = start_state
	i = 1
	for a in path:
		curr = curr.result(a)
		print('After %d move%s: %s' % (i, ("", "s")[i > 1], a))
		print(curr)

		input("Press return for the next state...")   # wait for key stroke
		i += 1
	return


if __name__ == '__main__':
	main()
