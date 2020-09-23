import unittest
from env import MarsRover
#from pe_monte_carlo import monte_carlo_step, evaluate_policy_mc
from solutions import monte_carlo_step, evaluate_policy_mc

class MyTestCase(unittest.TestCase):

    def test_members(self):
        with open('members.txt') as fh:
            lines = fh.readlines()

        self.assertTrue(lines[0].startswith('member 1: '))
        self.assertTrue(lines[1].startswith('member 2: '))
        self.assertTrue(lines[2].startswith('member 3: '))


if __name__ == '__main__':
    unittest.main()
