

class agentFVOWL:

    def __init__(self,config):
        self.config = config
        self.reset()

    def reset(self):
        self.all_letters = ['a','e','i','ı','u','o','ü','ö','l','k','m','r','t','n','s','b','y','d','ş','z','c','ç','p','g','h','v','f','ğ','j']

    def get_next_action(self,state):
        while self.all_letters[0] in state['guessed_letters']:
            self.all_letters.pop(0)
        return self.all_letters[0]