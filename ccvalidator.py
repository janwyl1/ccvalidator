#
# Validate Credit Card Numbers using the Luhn algorithm
# https://www.rosettacode.org/wiki/Luhn_test_of_credit_card_numbers
#
class CcVal:
    def __init__(self, cc):
        self.cc = str(cc)

    def luhn(self):
        s1 = 0
        s2 = 0
        for i, x in enumerate(self.cc[::-1]):
            if (int(i) % 2 == 0): 
                s1 += int(x)
            else:
                tot = 0
                dbl = int(x) * 2
                for j in str(dbl):
                    tot += int(j)
                s2 += tot
        if ((s1 + s2) % 10 == 0) :
            return True
        return False 

    def lenChk(self):
        if (len(self.cc) < 8 or len(self.cc) > 19):
            return False
        return True
