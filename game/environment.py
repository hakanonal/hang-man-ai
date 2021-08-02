import random
from enum import Enum

class GameResult(Enum):
    Playing = 0
    Win = 1
    Loose = 2

class environment:

    def __init__(self,config = {'max_try' : 10}):
        self.config = config
        self.reset()

    def reset(self):
        with open('data/word_list.txt') as f:
            lines = [line.rstrip() for line in f]
        r = random.randrange(len(lines))
        word_to_guess = lines[r].lower()
        letters_to_guess = list(word_to_guess)
        self.state = {
            'word_to_guess' : word_to_guess,
            'letters_to_guess': letters_to_guess,
            'guessed_letters' : [],  
            'board' : [letter if letter == ' ' else '_' for letter in letters_to_guess],
            'result' : GameResult.Playing,
            'last_message': '',
            'max_try' : self.config['max_try'],
            'try' : 0,
        }
    
    def play(self,letter):
        if(len(letter) > 1):
            self.state['last_message'] = 'Only one letter allowed!'
            return self.state

        if(letter.isalpha() == False):
            self.state['last_message'] = 'Invalid letter %s!' % letter
            return self.state

        letter = letter.lower()
        if letter in self.state['guessed_letters']:
            self.state['last_message'] = 'You have guessed the letter %s before!' % letter
            return self.state
        
        self.state['guessed_letters'].append(letter)
        
        _find_any = False
        for i, letter_to_guess in enumerate(self.state['letters_to_guess']):
            if(letter_to_guess == letter):
                self.state['board'][i] = letter
                _find_any = True
        
        if not _find_any:
            self.state['try'] += 1

        if '_' not in self.state['board']:
            self.state['last_message'] = 'You Won!'
            self.state['result'] = GameResult.Win
            return self.state

        if self.state['max_try'] <= self.state['try']:
            self.state['last_message'] = 'You Lost! The word was %s' % self.state['word_to_guess']
            self.state['board'] = self.state['letters_to_guess']
            self.state['result'] = GameResult.Loose
            return self.state

        self.state['last_message'] = 'Go on...'
        return self.state

    def board(self):
        return ''.join(self.state['board'])
