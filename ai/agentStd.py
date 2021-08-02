

class agentSTD:

    def __init__(self,config):
        self.config = config
        self.all_letters = ['abcçdefgğhıijklmnoöprsştuüvyz']


    def get_next_action(self,state):
        while self.all_letters[0] in state['guessed_letters']:
            self.all_letters.pop(0)
        return self.all_letters[0]