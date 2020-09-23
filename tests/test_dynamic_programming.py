import unittest
import numpy as np
from env import MarsRover
from pe_dynamic_programming import dynamic_programming_step, evaluate_policy_dp

class TestDP(unittest.TestCase):

    def test_dp_step(self):
        transition_probabilities=np.ones((5, 2))
        rewards = [1, 0, 0, 0, 10]
        v = np.zeros(5)
        pi = np.zeros(5)
        v_new = dynamic_programming_step(v, pi, transition_probabilities, rewards)
        self.assertFalse(np.array_equal(v, v_new))
        self.assertTrue(v_new[1] == 1)

        v = [1, 0, 0, 0, 0]
        v_new = dynamic_programming_step(v, pi, transition_probabilities, rewards, gamma=0.8)
        self.assertTrue(v_new[1] == 1.8)

        transition_probabilities=np.ones((5, 2))
        rewards = [0, 0, 0, 0, 0]
        v = np.zeros(5)
        v_new = dynamic_programming_step(v, pi, transition_probabilities, rewards)
        self.assertTrue(np.array_equal(v, v_new))

    def test_dp_eval(self):
        pi = np.zeros(5)
        v, i = evaluate_policy_dp(pi)
        self.assertTrue(i > 1)
        self.assertTrue(v[4]!=0)
        self.assertTrue(v[3]!=0)

        v, i = evaluate_policy_dp(pi, rewards=np.zeros(5))
        self.assertTrue(i == 1)

if __name__ == '__main__':
    unittest.main()
