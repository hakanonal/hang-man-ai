
from game.environment import environment
from game.environment import GameResult

def play():
    e = environment()

    while True:
        print('%s Left: %d %s %s'%(e.board(),e.state['max_try']-e.state['try'],e.state['guessed_letters'],e.state['last_message']))
        if e.state['result'] != GameResult.Playing:
            break
        c = input('Guess letter: ')
        e.play(c)

if __name__ == "__main__":
    play()