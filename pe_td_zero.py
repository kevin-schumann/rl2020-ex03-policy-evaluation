import numpy as np
from env import MarsRover

def td_zero_step(v, sample, alpha=0.1, gamma=0.9):
    return v_new

def evaluate_policy_td_zero(pi=np.random.randint(2, size=5), transition_probabilities=np.ones((5,2)), rewards=[1, 0, 0, 0, 10]):
    env = MarsRover(transition_probabilities=transition_probabilities, rewards=rewards)
    i = 0
    while not (v==v_new).all():
        ++i
    print(f"Policy was evaluated in {i} steps with resulting v {v}")
    return v, i
