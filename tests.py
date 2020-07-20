import solution
import unittest

class testPieSolution(unittest.TestCase):

    def tests(self):
        

        self.assertEqual(solution.solution("abcabcabcabc"), 4)
        # self.assertEqual(solution.solution("abccbaabccba"), 2)
    

if __name__ == '__main__':
    unittest.main()