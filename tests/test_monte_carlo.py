import unittest
import numpy as np
from env import MarsRover
from pe_monte_carlo import monte_carlo_step, evaluate_policy_mc

class TestMC(unittest.TestCase):

    def test_mc_step(self):
        sample = [2, 0, 0, 1, 0, 1, 0]
        v = np.zeros(5)
        g = np.zeros(5)
        n = np.zeros(5)
        v_new, n_new, g_new = monte_carlo_step(v, n, g, sample)
        self.assertTrue((n_new==[1, 1, 1, 0, 0]).all())
        self.assertTrue(g_new[1]==1)
        self.assertTrue(g_new[2]==0.9)
        self.assertFalse(np.array_equal(v, v_new))

        sample = [2, 0, 0, 1, 0, 0, 0]
        v = np.zeros(5)
        g = np.zeros(5)
        n = np.zeros(5)
        v_new, n_new, g_new = monte_carlo_step(v, n, g, sample)
        self.assertTrue((n_new==[1, 1, 1, 0, 0]).all())
        self.assertTrue(np.array_equal(v, v_new))

    def test_mc_eval(self):
        pi = np.zeros(5)
        v, i = evaluate_policy_mc(pi)
        self.assertTrue(i > 1)
        self.assertTrue(v[4]==0)
        self.assertTrue(v[3]==0)

        v, i = evaluate_policy_mc(pi, rewards=np.zeros(5))
        self.assertTrue(i == 1)

if __name__ == '__main__':
    unittest.main()
