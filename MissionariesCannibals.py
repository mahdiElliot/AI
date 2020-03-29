from collections import deque
import copy
import sys

from State import State
from Problem import Problem
from SimpleProblemSolvingAgentProgram import SimpleProblemSolvingAgentProgram

class MissionariesCannibals(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def actions(self, state):
        possible_actions = [(0, 1), (0, 2), (1, 0), (1, 1), (2, 0)]
        
        missionaries = state[0]
        cannibals = state[1]
        location = state[2]

        a = copy.deepcopy(possible_actions)
        if location == 'loc_A':
            for i in range(0, len(a)):
                if missionaries < a[i][0] or cannibals < a[i][1]:
                    possible_actions.remove(a[i])
        else:
            for i in range(0, len(a)):
                if missionaries + a[i][0] > 3 or cannibals + a[i][1] > 3:
                    possible_actions.remove(a[i])
        
        return possible_actions
    
    def result(self, state, action):
        new_state = list(state)

        if state[2] == 'loc_A':
            new_state[2] = 'loc_B'
            new_state[0] = state[0] - action[0]
            new_state[1] = state[1] - action[1]
        else:
            new_state[2] = 'loc_A'
            new_state[0] = state[0] + action[0]
            new_state[1] = state[1] + action[1]

        new_state[3] = state

        if self.check_possible_state(tuple(new_state)):
            return tuple(new_state)

    def goal_test(self, state):
        return self.goal[0] == state[0] and self.goal[1] == state[1] and self.goal[2] == state[2]

    def check_possible_state(self, new_state):
        missionaries = new_state[0]
        cannibals = new_state[1]
        
        tempState = copy.deepcopy(new_state)
        notEqual = True
        while tempState[3] != None:
            state = tempState[3]
            if state[0] == new_state[0] and state[1] == new_state[1] and state[2] == new_state[2]:
                notEqual = False
                break
            tempState = copy.deepcopy(state)
        
        return cannibals <= missionaries and notEqual
