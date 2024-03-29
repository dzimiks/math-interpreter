import unittest
from math_interpreter.calculator import prefix_calculation, infix_calculation, postfix_calculation
from math_interpreter.var_storage import VarStorage


class Test(unittest.TestCase):
    def test_prefix(self):
        var_storage = VarStorage()

        prefix_1 = prefix_calculation('+ + 1 * 2 3 4', var_storage)
        answer_1 = '11'

        prefix_2 = prefix_calculation('* + 1 2 + 3 4', var_storage)
        answer_2 = '21'

        prefix_3 = prefix_calculation('+ * 1 2 * 3 4', var_storage)
        answer_3 = '14'

        prefix_4 = prefix_calculation('+ + + 1 2 3 4', var_storage)
        answer_4 = '10'

        prefix_5 = prefix_calculation('+ RIM(MCDXV) 66', var_storage)
        answer_5 = '1481'

        prefix_6 = prefix_calculation('* + - / RIM(MDCCLXXVI) 3 11 2 16', var_storage)
        answer_6 = '9328'

        prefix_7 = prefix_calculation('> 55 4', var_storage)
        answer_7 = 'True'

        prefix_8 = prefix_calculation('>1 RIM(IX)', var_storage)
        answer_8 = 'False'

        prefix_9 = prefix_calculation('> <= 334 RIM(MD) 4', var_storage)
        answer_9 = 'True'

        prefix_10 = prefix_calculation('-= RIM RIM(XXX)                9', var_storage)
        answer_10 = '21'

        prefix_11 = prefix_calculation('RIM', var_storage)
        answer_11 = '30'

        prefix_12 = prefix_calculation('=hanica_123 4', var_storage)
        answer_12 = '4'

        prefix_13 = prefix_calculation('> ==hanica_123 4 3', var_storage)
        answer_13 = 'True'

        prefix_14 = prefix_calculation('+*1 2 3', var_storage)
        answer_14 = '5'

        prefix_15 = prefix_calculation('<=+10 20 29', var_storage)
        answer_15 = 'False'

        self.assertEqual(prefix_1, answer_1)
        self.assertEqual(prefix_2, answer_2)
        self.assertEqual(prefix_3, answer_3)
        self.assertEqual(prefix_4, answer_4)
        self.assertEqual(prefix_5, answer_5)
        self.assertEqual(prefix_6, answer_6)
        self.assertEqual(prefix_7, answer_7)
        self.assertEqual(prefix_8, answer_8)
        self.assertEqual(prefix_9, answer_9)
        self.assertEqual(prefix_10, answer_10)
        self.assertEqual(prefix_11, answer_11)
        self.assertEqual(prefix_12, answer_12)
        self.assertEqual(prefix_13, answer_13)
        self.assertEqual(prefix_14, answer_14)
        self.assertEqual(prefix_15, answer_15)

    def test_infix(self):
        var_storage = VarStorage()

        infix_1 = infix_calculation('10+RIM(XX) +        hana =RIM(M) +10', var_storage)
        answer_1 = '1040'

        infix_2 = infix_calculation('5 + y = 2 + 3 * 6', var_storage)
        answer_2 = '25'

        infix_3 = infix_calculation('2 + (y = 3) + 1', var_storage)
        answer_3 = '6'

        infix_4 = infix_calculation('y = 1 + 2 * 8 - 6', var_storage)
        answer_4 = '11'

        infix_5 = infix_calculation('4 * ( y = 5 + 8 * 6 ) / 7', var_storage)
        answer_5 = '30'

        infix_6 = infix_calculation('hana / y', var_storage)
        answer_6 = '19'

        self.assertEqual(infix_1, answer_1)
        self.assertEqual(infix_2, answer_2)
        self.assertEqual(infix_3, answer_3)
        self.assertEqual(infix_4, answer_4)
        self.assertEqual(infix_5, answer_5)
        self.assertEqual(infix_6, answer_6)

    def test_postfix(self):
        var_storage = VarStorage()

        postfix_1 = postfix_calculation('10 20 * 30 +', var_storage)
        answer_1 = '230'

        postfix_2 = postfix_calculation('10 200 + 30 40 + *', var_storage)
        answer_2 = '14700'

        postfix_3 = postfix_calculation('1 2 3 *+ 4 +', var_storage)
        answer_3 = '11'

        postfix_4 = postfix_calculation('1 2 + 3 4 + *', var_storage)
        answer_4 = '21'

        postfix_5 = postfix_calculation('1 2 * 3 4 * +', var_storage)
        answer_5 = '14'

        postfix_6 = postfix_calculation('1 2 + 3 + 4+', var_storage)
        answer_6 = '10'

        postfix_7 = postfix_calculation('RIM(MCDXV) 66 +', var_storage)
        answer_7 = '1481'

        postfix_8 = postfix_calculation('4 5 >', var_storage)
        answer_8 = 'False'

        postfix_9 = postfix_calculation('1 y 2 = +', var_storage)
        answer_9 = '3'

        postfix_10 = postfix_calculation('70 hana 10 = /', var_storage)
        answer_10 = '7'

        postfix_11 = postfix_calculation('hana', var_storage)
        answer_11 = '10'

        self.assertEqual(postfix_1, answer_1)
        self.assertEqual(postfix_2, answer_2)
        self.assertEqual(postfix_3, answer_3)
        self.assertEqual(postfix_4, answer_4)
        self.assertEqual(postfix_5, answer_5)
        self.assertEqual(postfix_6, answer_6)
        self.assertEqual(postfix_7, answer_7)
        self.assertEqual(postfix_8, answer_8)
        self.assertEqual(postfix_9, answer_9)
        self.assertEqual(postfix_10, answer_10)
        self.assertEqual(postfix_11, answer_11)


if __name__ == '__main__':
    unittest.main()
