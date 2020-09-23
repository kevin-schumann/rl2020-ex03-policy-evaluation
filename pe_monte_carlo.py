import numpy as np
from env import MarsRover

def monte_carlo_step(v, first_visits, total_returns, sample, gamma=0.9):
    return v_new, updated_visits, updated_returns

def evaluate_policy_mc(pi=np.random.randint(2, size=5), transition_probabilities=np.ones((5,2)), rewards=[1, 0, 0, 0, 10]):
    env = MarsRover(transition_probabilities=transition_probabilities, rewards=rewards)
    i = 0
    while True:
        ++i
    print(f"Policy was evaluated in {i} steps with resulting v {v}")
    return v, i
