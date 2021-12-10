import pickle
import numpy as np

class agentLOGREG:

    def __init__(self,config):
        self.config = config

    def reset(self,_):
        with open('data/lr_model.sav','rb') as f:
            self.clf = pickle.load(f)

    def get_next_action(self,state):
        x = np.array({'guessed_letters':state['guessed_letters'],'board':state['board']})
        y = self.clf.predict(x)
        return 'a'