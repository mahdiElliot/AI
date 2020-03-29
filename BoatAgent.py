from Agent import Agent
from Missionary import Missionary
from Cannibal import Cannibal
from Direction import Direction

class BoatAgent(Agent):
    def __init__(self, program=None):
        super().__init__(program)
        self.direction = Direction(Direction.R)
        self.capacity = 2
        self.location = 'loc_A'

    def can_grab(self, thing):
        return thing in (Missionary, Cannibal)


def ModelBasedReflexAgentProgram():
    """
    [Figure 2.12]
    This agent takes action based on the percept and state.
    """

    model = {'loc_A': None, 'loc_B': None}
    def program(percept):
        location = percept[0]
        status = percept[1]
        model[location] = status
        
    return BoatAgent(program)
