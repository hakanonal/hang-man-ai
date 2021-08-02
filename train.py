from ai.run import run

def train():
    config = {
        'discount': 0.95,
        'exploration_rate':0.9,
        'decay_factor':0.99,
        'learning_rate':0.001,
        'episode':10000,
        'debug' : 0,
        'max_try' : 29,
    }

    import os
    os.environ['WANDB_MODE'] = 'dryrun'

    r = run(config=config)

    r.start()


if __name__ == "__main__":
    train()