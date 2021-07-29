
class environment:

    def __init__(self):
        self.reset()

    def reset(self):
        word_to_guess = 'aba'.lower() #TODO: retrive from word list.
        letters_to_guess = list(word_to_guess)
        self.state = {
            'word_to_guess' : word_to_guess,
            'letters_to_guess': letters_to_guess,
            'guessed_letters' : [],  
            'board' : [letter if letter == ' ' else '_' for letter in letters_to_guess],
            'is_finised' : False,
            'last_message': '',
            'max_try' : 10,
            'try' : 0,
        }
    
    def play(self,letter):
        if(letter.isalpha() == False):
            self.state['last_message'] = 'Invalid letter %s!' % letter
            return self.state

        letter = letter.lower()
        if letter in self.state['guessed_letters']:
            self.state['last_message'] = 'You have guessed the letter %s before!' % letter
            return self.state
        
        self.state['guessed_letters'].append(letter)
        self.state['try'] += 1
        
        for i, letter_to_guess in enumerate(self.state['letters_to_guess']):
            if(letter_to_guess == letter):
                self.state['board'][i] = letter

        if '_' not in self.state['board']:
            self.state['last_message'] = 'You Won!'
            self.state['is_finised'] = True
            return self.state

        if self.state['max_try'] <= self.state['try']:
            self.state['last_message'] = 'You Lost! The word was %s' % self.state['word_to_guess']
            self.state['board'] = self.state['letters_to_guess']
            self.state['is_finised'] = True
            return self.state

        self.state['last_message'] = 'Ok'
        return self.state
