def quicksort(arr):
    if len(arr)<1:
        return arr
    less = []
    equal = []
    more = []
    pivot = arr[0]
    for i in arr:
        if i < pivot:
            less.append(i)
        if i == pivot:
            equal.append(i)
        if i > pivot:
            more.append(i)
    return quicksort(less) + equal + quicksort(more)

def countmax(arr):
    result = tmp = (None, 0)

    for a in quicksort(arr):
        if a == tmp[0]:
            print tmp
            tmp = (a, tmp[1] + 1)
        else:
            print tmp
            if tmp[1] > result[1]:
                result = tmp
                print result
            else:
                tmp = (a, 1)

    return result

def genwave(sarray):
    out = []
    while True:
            out.append(sarray.pop())
            out.append(sarray.pop(0))
    return out

if __name__ == '__main__':
    print 'quicksort',
    aaa = [1,2,2,2,2,2,3, 0,9,6,5,4,3, 4, 4,4,4,2,22,55,66,11,1,2,3,4,5,6]
    sss = 'quxicksoxxxxxrxxxtquiixiissxaabdxx'
    print quicksort(aaa)
    print countmax(aaa)
    print genwave(quicksort(aaa))
