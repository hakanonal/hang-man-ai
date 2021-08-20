from ai.run import run
import wandb

def sweep():
    r = run()
    r.start()


wandb.agent('hakanonal/hang-man-ai/v0l2e7i3',function=sweep)
