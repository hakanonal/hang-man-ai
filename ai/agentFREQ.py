

class agentFREQ:

    def __init__(self,config):
        self.config = config
        self.reset()

    def reset(self):
        self.all_letters = ['a','e','l','i','k','m','r','ı','t','n','s','u','b','y','d','ş','o','z','ü','c','ç','p','g','h','v','f','ğ','ö','j']

    def get_next_action(self,state):
        while self.all_letters[0] in state['guessed_letters']:
            self.all_letters.pop(0)
        return self.all_letters[0]