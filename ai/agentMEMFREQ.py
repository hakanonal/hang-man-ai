

class agentMEMFREQ:

    def __init__(self,config):
        self.config = config

    def reset(self,state):
        with open('data/word_list.txt') as f:
            lines = [line.rstrip() for line in f]        
        narrowed_lines = [line for line in lines if len(line) == len(state['letters_to_guess'])]

        d = []
        for line in narrowed_lines:
            for letter in list(line):
                if letter != ' ':
                    d.append(letter.lower())
        d.sort()            
        histogram = [(x,d.count(x)) for x in set(d)]
        sorted_histogrram = sorted(histogram, key=lambda tup: tup[1], reverse=True)
        self.all_letters = [tup[0] for tup in sorted_histogrram] 

    def get_next_action(self,state):
        while self.all_letters[0] in state['guessed_letters']:
            self.all_letters.pop(0)
        return self.all_letters[0]