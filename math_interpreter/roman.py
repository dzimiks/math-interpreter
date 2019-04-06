M, D, C, L, X, V, I = ('M', 'D', 'C', 'L', 'X', 'V', 'I')
roman_dict = {M: 1000, D: 500, C: 100, L: 50, X: 10, V: 5, I: 1}


class Roman:
    def __init__(self):
        self.text = ''
        self.pos = 0

    def big_production(self, small, mid, big):
        """
        HUNDREDS -> SMALL_HUNDREDS {return SMALL_HUNDREDS} | CD {return 400} |
                    D SMALL_HUNDREDS {return 500 + SMALL_HUNDREDS} | CM {return 900}
        TENS ->     SMALL_TENS {return SMALL_TENS} | XL {return 40} |
                    L SMALL_TENS {return 50 + SMALL_TENS} | XC {return 90}
        DIGITS ->   SMALL_DIGITS {return SMALL_DIGITS} | IV {return 4} |
                    V SMALL_DIGITS {return 5 + SMALL_DIGITS} | IX {return 9}
        """

        if self.get_current_char() == small:
            self.pos += 1

            if self.get_current_char() == mid:
                self.pos += 1
                return roman_dict[mid] - roman_dict[small]
            elif self.get_current_char() == big:
                self.pos += 1
                return roman_dict[big] - roman_dict[small]
            else:
                self.pos -= 1
                return self.small_production(small)
        elif self.get_current_char() == mid:
            self.pos += 1
            return roman_dict[mid] + self.small_production(small)
        else:
            return 0

    def small_production(self, small):
        """
        SMALL_HUNDREDS ->   C {return 100} | CC {return 200} | CCC {return 300} | e {return 0}
        SMALL_TENS ->       X {return 10} | XX {return 20} | XXX {return 30} | e {return 0}
        SMALL_DIGITS ->     I {return 1} | II {return 2} | III {return 3} | e {return 0}
        """

        result = 0

        for i in range(3):
            if self.get_current_char() == small:
                result += roman_dict[small]
                self.pos += 1
            else:
                return result

        return result

    def has_next(self):
        if not self.pos > len(self.text) - 1:
            return True

        return False

    def get_current_char(self):
        if self.has_next():
            return self.text[self.pos]

        return None

    def roman(self, text):
        """
        ROMAN -> THOUSANDS HUNDREDS TENS DIGITS {return THOUSANDS + HUNDREDS + TENS + DIGITS}
        """
        self.text = text
        self.pos = 0

        thousands = self.small_production(M)
        hundreds = self.big_production(C, D, M)
        tens = self.big_production(X, L, C)
        digits = self.big_production(I, V, X)

        return thousands + hundreds + tens + digits


def main():
    roman = Roman()
    print(roman.roman('MMI'))
    print(roman.roman('X'))
    print(roman.roman('XIX'))
    print(roman.roman('VI'))
    print(roman.roman('IV'))
    print(roman.roman('MCD'))
    print(roman.roman('MCMLXXXIV'))
    print(roman.roman('IX'))
    print(roman.roman('MMM'))
    print(roman.roman('DCCCLXXXVIII'))
    print(roman.roman('MMMDCCCXXXIII'))
    print(roman.roman('MMMDCCCXXVIII'))
    print(roman.roman('MMMDCCCLXXXVIII'))


if __name__ == '__main__':
    main()
