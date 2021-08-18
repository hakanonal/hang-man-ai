

class agentSTD:

    def __init__(self,config):
        self.config = config

    def reset(self,_):
        self.all_letters = ['a','b','c','ç','d','e','f','g','ğ','h','ı','i','j','k','l','m','n','o','ö','p','r','s','ş','t','u','ü','v','y','z']

    def get_next_action(self,state):
        while self.all_letters[0] in state['guessed_letters']:
            self.all_letters.pop(0)
        return self.all_letters[0]