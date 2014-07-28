'1 *2 +1 *2 +1 ...'
'1 2 3 6 7'
'n+1 n*2 n+1'

import sys
import fileinput

""" The Utopian tree goes through 2 cycles of growth every year.
The first growth cycle of the tree is during the monsoon season when it doubles in height.
The second growth cycle is during the summer when it increases in height by 1 meter.
If a new Utopian tree sapling of height 1 meter is planted just before the onset of the monsoon season,
can you find the height of the tree after N cycles?
"""

def growth(n):
    h = 1
    if n == 0:
        return h

    for i in range(n):
        year = i+1
        if year % 2 == 0:
            h += 1
        else:
            h *= 2
    return h





arr = sys.stdin.readlines()
tc = int(arr[0])
inputs = [int(i) for i in arr[1:]]

for i in range(tc):
    print growth(inputs[i])
