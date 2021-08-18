from game.environment import environment
from game.environment import GameResult
import wandb

from .agentSTD import agentSTD
from .agentFREQ import agentFREQ
from .agentFVOWL import agentFVOWL
from .agentMEMFREQ import agentMEMFREQ


agentmap = {
    'agentSTD': agentSTD,
    'agentFREQ': agentFREQ,
    'agentFVOWL': agentFVOWL,
    'agentMEMFREQ': agentMEMFREQ,
}

class run:
    def __init__(self, config=None):
        if(config is None):
            wandb.init(project="hang-man-ai")
            self.config = wandb.config
        else:
            wandb.init(project="hang-man-ai",config=config)
            self.config = config
        self.metrics = {
            'tot_try' : 0,
        }
        self.agent = agentmap[self.config['agent']](self.config)
        self.environment = environment(self.config)


    def start(self):
        for episode in range(1,self.config['episode']+1):
            #Begin Game
            self.environment.reset()
            self.agent.reset(self.environment.state)

            #Playing
            while self.environment.state['result'] == GameResult.Playing:
                old_state = self.environment.state
                action_to_play = self.agent.get_next_action(old_state)
                new_state = self.environment.play(action_to_play)

            #Sending Metrics
            self.metrics['tot_try'] += self.environment.state['try']
            self.metrics['avg_try'] = self.metrics['tot_try'] / episode
            wandb.log(self.metrics,step=episode)
