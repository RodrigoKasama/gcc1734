# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """

        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    # Etapas:
        1. Define o estado inicial do problema
        2. Definimos a fronteira
        3. Definimos a coleção de nós que já foram visitados

        # Enquanto a fronteira não está vazia (todos os estados percorridos
                Removemos ele da fronteira
                Ele já foi explorado? Se sim, próxima iteração
                Adicionamos a coleção de nós visitados...(Marcamos como percorrido)
                Se ele é o objetivo buscado, então retornar o plano até esse estado (getActionSequence(node)) FIM

                Como esse nó não nos interessa mais, adicionamos a lista de 'childs' desse nó à fronteira e seguimos em frente

        return []; // Se retornou isso DEVE estar errado...

    """

    initialNode = getStartNode(problem)

    frontier = util.Stack()  # LIFO

    # Add a raiz a fronteira --> Primeiro nó a se explorar
    frontier.push(initialNode)

    # Nós visitados representa um conjunto de nós (não há repetição)
    nos_visitados = set()

    # Enquanto a frontera (Stack) não está vazia
    while not frontier.isEmpty():

        # Seleciona e remove o último nó add a fronteira? Não deveria ser o mais custoso?
        curr_no = frontier.pop()
        curr_state = curr_no["STATE"]  # Coleta o estado desse nó

        if curr_state in nos_visitados:
            continue

        nos_visitados.add(curr_state)

        if problem.isGoalState(curr_state):
            return getActionSequence(curr_no)

        for no_filho in problem.expand(curr_state):
            child_no = getChildNode(no_filho, curr_no)
            frontier.push(child_no)
    return []

    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # input("aaa")


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# *********************************************************************************************************************************************************************


def getStartNode(problem):
    return {"STATE": problem.getStartState(), "PATH-COST": 0}


def getChildNode(sucessor, parent_node):
    child_node = {'STATE': sucessor[0], 'PARENT': parent_node,
                  'ACTION': sucessor[1], 'PATH-COST': parent_node['PATH-COST'] + sucessor[2]}
    return child_node


def getActionSequence(node):
    actions = []
    while node['PATH-COST'] > 0:
        actions.insert(0, node['ACTION'])
        node = node['PARENT']
    return actions


# *********************************************************************************************************************************************************************
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
