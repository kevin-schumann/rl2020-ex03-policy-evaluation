import unittest

class TestQuestions(unittest.TestCase):

    def testQuestions(self):
        with open('observations.txt') as fh:
            lines = fh.readlines()

        self.assertTrue(lines[0].startswith('Dyn') or lines[0].startswith('dyn'))
        self.assertTrue(lines[1].startswith('T') or lines[1].startswith('t') or lines[1].startswith('M') or lines[1].startswith('m'))

if __name__ == '__main__':
    unittest.main()
