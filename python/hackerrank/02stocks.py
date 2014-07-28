import sys


def sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [i for i in arr if i < pivot]
    equal = [ i for i in arr if i == pivot]
    right = [ i for i in arr if i > pivot]
    return sort(left) + equal + sort(right)

def trader(days, prices):
    cost = 0
    shares = 0




arr = sys.stdin.readlines()
tc = int(arr[0])
inputs = [i for i in arr[1:]]

# 2 lines per TC
for i in range(tc):
    index = i * 2
    days = inputs[index]
    prices = [ int(x) for x in inputs[index+1].split(' ')]
    print trader(days, prices)


