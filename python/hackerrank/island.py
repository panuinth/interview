import json

def count_island(input):
    if not isinstance(input, list):
        return 0

    count = 0
    visit = input[:]
    for j in range(len(input)):
        for i in range(len(input[j])):
            if visit[j][i] == 1 and input[j][i] == 1:
                DFS(i, j, visit)
                count += 1

    return count

def DFS(i, j, visit):
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    for d in directions:
        if (0 <= i+d[0] <= len(visit[j])-1 and
            0 <= j+d[1] <= len(visit) -1 and
            visit[j + d[1]][i + d[0]] == 1):
            visit[j + d[1]][i + d[0]] = False
            DFS(i + d[0], j + d[1], visit)
    return



def test():
    input = [   [1, 1, 0, 0, 0],
                [0, 1, 0, 0, 1],
                [1, 0, 0, 1, 1],
                [0, 0, 0, 0, 0],
                [1, 0, 1, 0, 1]
        ]

    print count_island(input)

def tests2():
    input = [   [1, 0, 1, 1, 1, 0],
                [0, 0, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 1],
        ]

    print count_island(input)

tests2()

def fix_test():
    input = list()
    for i in range(1000000):
        input.append(i % 2)

    print count_island([input])

print 'xx'*20
fix_test()



def neg_test():
    inputs = [None, [], [[]]]
    for i in inputs:
        print count_island(i)

neg_test()
