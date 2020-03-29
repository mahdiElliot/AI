from Environmnet import Environment
from Missionary import Missionary
from Cannibal import Cannibal
from Thing import Thing
from BoatAgent import BoatAgent

class MissionariesCannibalsEnv(Environment):
    def __init__(self):
        super().__init__()
        #[missionaries, cannibals]
        self.status = {'loc_A': [3, 3],
                        'loc_B': [0, 0]} 

    def thing_classes(self):
        return [Missionary, Cannibal, BoatAgent]
    
    def env_things(self, agent):
        things = []
        for t in self.thing_classes():
            if agent.can_grab(t):
                things.append(t)

        return things

    def percept(self, agent):

        return (agent.location, self.status[agent.location],
                agent.holding, agent.capacity)

    def default_location(self, thing):
        return 'loc_A'
        
    def execute_action(self, agent, action):
        pass
