"""
convert Roman to Int
     case 'I': return 1;
     case 'V': return 5;    ( never be subtract)
     case 'X': return 10;
     case 'L': return 50;   ( never be subtract)
     case 'C': return 100;
     case 'D': return 500;  ( never be subtract)
     case 'M': return 1000;
     default: return 0;


if lower digit come before higher,  user (higher - lower)


"""

mapping = [
            ('M', 1000),
            ('CM', 900),
            ('D', 500),
            ('CD', 400),
            ('C', 100),
            ('XC', 90),
            ('L', 50),
            ('XL', 40),
            ('X', 10),
            ('IX', 9),
            ('V', 5),
            ('IV', 4),
            ('I', 1),
           ]


class Solution:
    # @return an integer
    def romanToInt(self, s):
        result = 0
        index = 0
        for symbol, value in mapping:
            while s[index:index+len(symbol)] == symbol:
                result += value
                index += len(symbol)
        return result


def test():
    for i in [ 'MDCLXIXVI']:
        print Solution().romanToInt(i)

test()
