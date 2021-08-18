

class agentMEMFREQv2:

    def __init__(self,config):
        self.config = config

    def reset(self,state):
        with open('data/word_list.txt') as f:
            self.lines = [line.rstrip() for line in f]  
        self.narrowed_lines = [line.lower() for line in self.lines if len(line) == len(state['letters_to_guess'])]                  

    def narrow_more(self,state):
        self.narrowed_more = []
        for line in self.narrowed_lines:
            consider_this_line = True
            for i in range(len(state['letters_to_guess'])):
                if state['board'][i] == '_':
                    continue
                if state['board'][i] != line[i]:
                    consider_this_line = False
                    continue
            if consider_this_line:
                self.narrowed_more.append(line)

    
    def update_all_letters(self):        
        d = []
        for line in self.narrowed_more:
            for letter in list(line):
                if letter != ' ':
                    d.append(letter.lower())
        d.sort()            
        histogram = [(x,d.count(x)) for x in set(d)]
        sorted_histogrram = sorted(histogram, key=lambda tup: tup[1], reverse=True)
        self.all_letters = [tup[0] for tup in sorted_histogrram] 

    def get_next_action(self,state):
        self.narrow_more(state)
        self.update_all_letters()
        while self.all_letters[0] in state['guessed_letters']:
            self.all_letters.pop(0)
        return self.all_letters[0]