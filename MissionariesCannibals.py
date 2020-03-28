from collections import deque
import sys

from Problem import Problem
from SimpleProblemSolvingAgentProgram import SimpleProblemSolvingAgentProgram

class MissionariesCannibals(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def actions(self, state):
        possible_actions = ['left', 'right', ('take', 'm', 1), ('take', 'm', 2),
                            ('take', 'c', 1), ('take', 'c', 2), ('put', 'm', 1),
                            ('put', 'm', 2), ('put', 'c', 1), ('put', 'c', 2)]
        
        if state[0] == 'loc_A':
            self.remove('left', possible_actions)
        else:
            self.remove('right', possible_actions)

        status = state[1]
        self.__missionariesActions(status, possible_actions)

        self.__cannibalsActions(status, possible_actions)
            
        self.__capacityActions(len(state[3]), possible_actions)

        return possible_actions

    def remove(self,x , possibleActions):
        if x in possibleActions:
            possibleActions.remove(x)
    
    def __missionariesActions(self, status, possible_actions):
        if status[0] < 2: #missionaries
            self.remove(('take', 'm', 2), possible_actions)
            if status[0] < 1:
                self.remove(('take', 'm', 1), possible_actions)
        else:
            self.remove(('put', 'm', 2), possible_actions)
            if status[0] > 2:
                self.remove(('put', 'm', 1), possible_actions)

    def __cannibalsActions(self, status, possible_actions):
        if status[1] < 2: #cannibals
            self.remove(('take', 'c', 2), possible_actions)
            if status[1] < 1:
                self.remove(('take', 'c', 1), possible_actions)
        else:
            self.remove(('put', 'c', 2), possible_actions)
            if status[1] > 2:
                self.remove(('put', 'c', 1), possible_actions)

    def __capacityActions(self, remainCapacity, possible_actions):
        if remainCapacity > 0:
            self.remove(('take', 'm', 2), possible_actions)
            self.remove(('take', 'c', 2), possible_actions)
            if remainCapacity > 1:
                self.remove(('take', 'm', 1), possible_actions)
                self.remove(('take', 'c', 1), possible_actions)
            else:
                self.remove(('put', 'm', 2), possible_actions)
                self.remove(('put', 'c', 2), possible_actions)
        else:
            self.remove(('put', 'm', 1), possible_actions)
            self.remove(('put', 'c', 1), possible_actions)
            self.remove(('put', 'm', 2), possible_actions)
            self.remove(('put', 'c', 2), possible_actions)

    def result(self, state, action):
        new_state = list(state)
        if action == 'right':
            new_state[0] = 'loc_B'
        elif action == 'left':
            new_state[0] = 'loc_A'
        elif action == ('take', 'm', 1):
            missionaries = new_state[1][0]
            if missionaries > 0:
                new_state[3].append('m')
                new_state[1][0] -= 1
        elif action == ('take', 'm', 2):
            missionaries = new_state[1][0]
            if missionaries > 1:
                new_state[3].append('m')
                new_state[3].append('m')
                new_state[1][0] -= 2
        elif action == ('take', 'c', 1):
            cannibals = new_state[1][1]
            if cannibals > 0:
                new_state[3].append('c')
                new_state[1][1] -= 1
        elif action == ('take', 'c', 2):
            cannibals = new_state[1][1]
            if cannibals > 1:
                new_state[3].append('c')
                new_state[3].append('c')
                new_state[1][1] -= 2
        elif action == ('put', 'm', 1):
            if 'm' in new_state[3]:
                new_state[3].remove('m')
                new_state[1][0] += 1
        elif action == ('put', 'm', 2):
            if new_state[3].count('m') > 1:
                new_state[3].remove('m')
                new_state[3].remove('m')
                new_state[1][0] += 2
        elif action == ('put', 'c', 1):
            if 'c' in new_state[3]:
                new_state[3].remove('c')
                new_state[1][1] += 1
        elif action == ('put', 'c', 2):
            if new_state[3].count('c') > 1:
                new_state[3].remove('c')
                new_state[3].remove('c')
                new_state[1][1] += 2

        if self.check_possible_state(new_state):
            return tuple(new_state)

    def goal_test(self, state):
        return state == self.goal

    def check_possible_state(self, state):
        missionaries = state[1][0]
        cannibals = state[1][1]
        return cannibals <= missionaries and len(state[3]) <= 2

            