
from environment import environment
from environment import GameResult

def main():
    e = environment()

    while True:
        print('%s Left: %d %s'%(e.board(),e.state['max_try']-e.state['try'],e.state['last_message']))
        if e.state['result'] != GameResult.Playing.Playing:
            break
        c = input('Guess letter: ')
        e.play(c)

if __name__ == "__main__":
    main()