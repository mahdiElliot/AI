from SimpleProblemSolvingAgentProgram import SimpleProblemSolvingAgentProgram
from MissionariesCannibals import MissionariesCannibals
from MissionariesCannibalsEnv import MissionariesCannibalsEnv
from Cannibal import Cannibal
from Missionary import Missionary
from BoatAgent import BoatAgent
from Node import Node
from State import State

from collections import deque

class SolvingBoatAgentProgram(SimpleProblemSolvingAgentProgram):
    def __init__(self, initial_state=None):
        super().__init__(initial_state)
    
    def update_state(self, state, percept):
        location, status, holding, capacity = percept
        return (status[0], status[1], location, state)

    def formulate_goal(self, state):
        goal = (0, 0, 'loc_B', None)
        return goal

    def formulate_problem(self, state, goal):
        problem = MissionariesCannibals(state, goal)
        return problem

    def search(self, problem):
        return self.iterative_deepending_tree_search(problem)

    def breath_first_tree_search(self, problem):
        frontier = deque([Node(problem.initial)])  # FIFO queue
        while frontier:
            node = frontier.popleft()
            if problem.goal_test(node.state):
                return node
            frontier.extend(node.expand(problem))
        return None

    def depth_first_limited_tree_search(self, problem, limit):

        frontier = [Node(problem.initial)]  # Stack

        while frontier:
            node = frontier.pop()
            if problem.goal_test(node.state):
                return node
            elif node.depth == limit:
                return 'cutoff'
            else:
                frontier.extend(node.expand(problem))
        return None

    def iterative_deepending_tree_search(self, problem):
        depth = 0
        while True:
            result = self.depth_first_limited_tree_search(problem, depth)
            print(depth)
            if result != 'cutoff':  return result
            depth += 1



environment = MissionariesCannibalsEnv()
environment.add_thing(Cannibal(), 'loc_A')
environment.add_thing(Cannibal(), 'loc_A')
environment.add_thing(Cannibal(), 'loc_A')
environment.add_thing(Missionary(), 'loc_A')
environment.add_thing(Missionary(), 'loc_A')
environment.add_thing(Missionary(), 'loc_A')
boatAgent = BoatAgent(None)
environment.add_thing(boatAgent)
percept = environment.percept(boatAgent)
solve = SolvingBoatAgentProgram(None)

node = solve.find(percept)
if node != None:
    print(node.solution())


