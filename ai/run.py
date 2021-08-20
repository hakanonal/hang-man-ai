from game.environment import environment
from game.environment import GameResult
import wandb

from .agentSTD import agentSTD
from .agentFREQ import agentFREQ
from .agentFVOWL import agentFVOWL
from .agentMEMFREQ import agentMEMFREQ
from .agentMEMFREQv2 import agentMEMFREQv2


agentmap = {
    'agentSTD': agentSTD,
    'agentFREQ': agentFREQ,
    'agentFVOWL': agentFVOWL,
    'agentMEMFREQ': agentMEMFREQ,
    'agentMEMFREQv2': agentMEMFREQv2,
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
            'max_try' : 0,
            'min_try' : self.config['max_try'],
        }
        self.agent = agentmap[self.config['agent']](self.config)
        self.environment = environment(self.config)


    def start(self):
        for episode in range(1,self.config['episode']+1):
            #Begin Game
            self.environment.reset(self.config['word_to_guess'])
            self.agent.reset(self.environment.state)

            #Playing
            while self.environment.state['result'] == GameResult.Playing:
                old_state = self.environment.state
                action_to_play = self.agent.get_next_action(old_state)
                new_state = self.environment.play(action_to_play)

            #Sending Metrics
            self.metrics['tot_try'] += self.environment.state['try']
            self.metrics['avg_try'] = self.metrics['tot_try'] / episode
            self.metrics['max_try'] = max(self.environment.state['try'],self.metrics['max_try'])
            self.metrics['min_try'] = min(self.environment.state['try'],self.metrics['min_try'])
            wandb.log(self.metrics,step=episode)
