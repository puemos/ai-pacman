# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def graphSearch(problem, frontier):
    """page n. 77 in the book."""
    # init the frontier using the init state of problem
    frontier.push((problem.getStartState(), []))
    # init the explored set to be empty
    explored = []
    # if the frontier and we didn't get
    # any solution we failed
    while not frontier.isEmpty():
        # choose a leaf node and remove it from the frontier
        state, actions = frontier.pop()
        # if the node contains a goal state return the solution
        if problem.isGoalState(state):
            return actions
        if state not in explored:
            # add the node is not in the explored
            explored.append(state)
            # expand the chosen node, adding the result
            # nodes that is not in the explored to the frontier
            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in explored:
                    next_actions = actions + [action]
                    successor_node = (successor, next_actions)
                    frontier.push(successor_node)

    return []


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """page n. 85 3.4.3"""
    # use LIFO and graphSearch
    frontier = util.Stack()
    return graphSearch(problem, frontier)


def breadthFirstSearch(problem):
    """page n. 85 3.4.3"""
    # use FIFO and graphSearch
    def costFn((state, actions)):
        return len(actions)
    # use FIFO and graphSearch
    frontier = util.PriorityQueueWithFunction(costFn)
    frontier.push((problem.getStartState(), []))
    return graphSearch(problem, frontier)


def uniformCostSearch(problem):
    """page n. 85 3.4.3"""
    # use the problem cost function
    def costFn((state, actions)):
        return problem.getCostOfActions(actions)
    # use FIFO and graphSearch
    frontier = util.PriorityQueueWithFunction(costFn)
    return graphSearch(problem, frontier)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    def costFn((state, actions)):
        return problem.getCostOfActions(actions) + heuristic(state, problem)
    frontier = util.PriorityQueueWithFunction(costFn)
    return graphSearch(problem, frontier)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
