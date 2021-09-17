from ai.run import run

def tournament():
    config = {
        'episode':10000,
        'max_try' : 29,
        'agent': 'agentRND',
        'word_to_guess' : False,
    }

    #import os
    #os.environ['WANDB_MODE'] = 'dryrun'

    r = run(config=config)

    r.start()


if __name__ == "__main__":
    tournament()