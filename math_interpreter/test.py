import unittest
from math_interpreter.mode import prefix_calculation, postfix_calculation


class Test(unittest.TestCase):
    def test_prefix(self):
        prefix_1 = prefix_calculation('+ + 1 * 2 3 4')
        answer_1 = '11'

        prefix_2 = prefix_calculation('* + 1 2 + 3 4')
        answer_2 = '21'

        prefix_3 = prefix_calculation('+ * 1 2 * 3 4')
        answer_3 = '14'

        prefix_4 = prefix_calculation('+ + + 1 2 3 4')
        answer_4 = '10'

        prefix_5 = prefix_calculation('+ RIM(MCDXV) 66')
        answer_5 = '1481'

        prefix_6 = prefix_calculation('* + - / RIM(MDCCLXXVI) 3 11 2 16')
        answer_6 = '9328'

        prefix_7 = prefix_calculation('> 55 4')
        answer_7 = 'True'

        prefix_8 = prefix_calculation('> 1 RIM(IX)')
        answer_8 = 'False'

        self.assertEqual(prefix_1, answer_1)
        self.assertEqual(prefix_2, answer_2)
        self.assertEqual(prefix_3, answer_3)
        self.assertEqual(prefix_4, answer_4)
        self.assertEqual(prefix_5, answer_5)
        self.assertEqual(prefix_6, answer_6)
        self.assertEqual(prefix_7, answer_7)
        self.assertEqual(prefix_8, answer_8)

    def test_postfix(self):
        postfix_1 = postfix_calculation('10 20 * 30 +')
        answer_1 = '230'

        postfix_2 = postfix_calculation('10 200 + 30 40 + *')
        answer_2 = '14700'

        postfix_3 = postfix_calculation('1 2 3 * + 4 +')
        answer_3 = '11'

        postfix_4 = postfix_calculation('1 2 + 3 4 + *')
        answer_4 = '21'

        postfix_5 = postfix_calculation('1 2 * 3 4 * +')
        answer_5 = '14'

        postfix_6 = postfix_calculation('1 2 + 3 + 4 +')
        answer_6 = '10'

        postfix_7 = postfix_calculation('RIM(MCDXV) 66 +')
        answer_7 = '1481'

        postfix_8 = postfix_calculation('4 5 >')
        answer_8 = 'False'

        self.assertEqual(postfix_1, answer_1)
        self.assertEqual(postfix_2, answer_2)
        self.assertEqual(postfix_3, answer_3)
        self.assertEqual(postfix_4, answer_4)
        self.assertEqual(postfix_5, answer_5)
        self.assertEqual(postfix_6, answer_6)
        self.assertEqual(postfix_7, answer_7)
        self.assertEqual(postfix_8, answer_8)


if __name__ == '__main__':
    unittest.main()

# print('INFIX')
# print('1 + 2 * 3 + 4 = ', 1 + 2 * 3 + 4)
# print('(1 + 2) * (3 + 4) = ', (1 + 2) * (3 + 4))
# print('1 * 2 + 3 * 4 = ', 1 * 2 + 3 * 4)
# print('1 + 2 + 3 + 4 = ', 1 + 2 + 3 + 4)
# print()
#
# print('PREFIX')
# prefix_calculation('+ + 1 * 2 3 4')
# prefix_calculation('* + 1 2 + 3 4')
# prefix_calculation('+ * 1 2 * 3 4')
# prefix_calculation('+ + + 1 2 3 4')
# prefix_calculation('= + 3 9 y')
# prefix_calculation('+ RIM(MCDXV) 66')
# print()
#
# print('POSTFIX')
# postfix_calculation('10 20 * 30 +')
# postfix_calculation('10 200 + 30 40 + *')
# postfix_calculation('1 2 3 * + 4 +')
# postfix_calculation('1 2 + 3 4 + *')
# postfix_calculation('1 2 * 3 4 * +')
# postfix_calculation('1 2 + 3 + 4 +')
# postfix_calculation('y 9 3 + =')
# postfix_calculation('RIM(MCDXV) 66 +')
# postfix_calculation('1 y 2 = +')
