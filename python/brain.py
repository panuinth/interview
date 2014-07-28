print """You and opponent alternate picking gold pots out of line. You can pick either
from the left or the right. All amounts of gold in all pots are know.
Write an algorithm to pick the most gold.
Assume you opponent is using the same algorithm
"""

def pick_gold(data):
    """ 1. return the sum, order of picking the gold pot
        2.
    """
    print data
    return sum(data)


arr = [1, 5,2,4,6,0, 9, 23,44]
print pick_gold(arr)



"""
Invert a Map e.g 1: {a,b} 2: {c,d} becomes a:1 b:1 c:2 d2"
"""
d = { 1: {'a', 'b'},
     2: {'c', 'd'}
     }

def invert_map(d):
    new_dict = dict()
    for i in d:
        for j in d[i]:
            new_dict[j] = i
    return new_dict

print invert_map(d)
