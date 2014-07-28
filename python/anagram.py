def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist, first, last):

    if first<last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)


def partition(alist, first, last):
    print first, last
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and \
               alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and \
                rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

        temp = alist[first]
        alist[first] = alist[rightmark]
        alist[rightmark] = temp


    return rightmark




def isAnagram(a, b):
    return quickSort([i for i in a]) == quickSort([i for i in b])

#print isAnagram('anagram', 'anagamr')

"""
length of the longest substring without repeating
"""

def longest_unique_substr(s):
    """ keep tracking of unique number, and total longest chars.
    """
    pre = 0
    d = {}
    for i in range(len(s)):
        if not s[i] in d:
            d[s[i]] = i
        else:
            pre = max(pre, len(d))
            d = dict()
    return max(pre, len(d))


s = 'aeebcdeefghijksssee'
print len(s)
print longest_unique_substr(s)


def longest_common_substr(s):
    """ keep tracking longest common string, if even return the first
    """
    c = ""
    l = 0
    result = (c, l)
    for i in range(len(s)):
        if s[i] == c:
            l += 1
        else:
            if l > result[1]:
                result = (c, l)
            l = 1
        c = s[i]
    return result


print len(s)
print longest_common_substr(s)

s = 'aaabbbdddd'

def count_repetition_in_array_int_order(s):
    s = sorted(s)
    pre = None
    count = 1
    out = list()
    for i in s:
        if pre is None:
            count = 1
            pre = i
        elif pre != i:
            out.append((pre,count))
            pre = i
            count = 1
        else:
            count += 1
    out.append((pre, count))
    return out


def count_repeat(s):
    s = sorted(s)
    count = 0
    c = None
    output = (c, count)
    for i in s:
        if c is None:
            c = i
            count = 1
        elif c != i:
            if output[1] < count:
                output = (c, count)
            c = i
            count =1
        else:
            count += 1
    return output








"""
1. Count the number of repetition of any value in the array of int.
"""
s = 'akjsdaineafdjbadpebfjasdkgasgenbdflkjdfabfaadslkjadgbewakdngkjbd'
print s
print  count_repetition_in_array_int_order(s)
print count_repeat(s)


"""
Consider the following array {1,2,3,4,5,2,5,4,4};
In the above array, index 4 could be considered as breaking point where
summation of 0 to 4 in the array is equal to summation of 5 to end of array.
We need to find the breaking point for the given array.
I solved this. But follow up was for this array


{1,0,-1,-1,1};
. Mathematically the later array's breaking point is 2.
"""

def breaking_point_bad(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) > sum(arr[i+1:]):
            print sum(arr[:i]), sum(arr[i:])
            print arr[:i], arr[i:]
            return i - 1

def breaking_point(arr):
    s0 = 0
    s1 = sum(arr)

    for i in arr:
        s0 += i
        s1 -= i
        if s0 == s1:
            return i


arr = [1,2,3,4,5,2,5,4,4]
arr = [1,0,-1,-1,1]

#print breaking_point(arr)


def matches(s1, pattern):
    """single star pattern"""
    if pattern.startswith('*'):
        return s1[len(pattern)+1:] == pattern[1:]
    elif pattern.endswith('*'):
        return s1[:len(pattern)-1] == pattern[:-1]
    elif '*' in pattern:
        index = pattern.index('*')
        return s1[:index]+s1[index+1] == pattern.replace('*', '')
    else:
        return s1 == pattern


print matches("index.html", "*html")
print matches("foo.txt", "*html")
print matches("casssst", "c*t")

print matches('abscjfdlfjdjfdafljdalfjdlafj', "abs*")





print """
1. Given a N different open and close braces in a string "( { [ } ] )". How do you check whether the string has matching braces.
"""


def validateBracket(s):
    """ validate bracket if it 's valid open/close bracket, accepted () {} []
    """
    print s
    stack = []
    for i in s:
        if i in '({[':
            stack.append(i)
        elif i in ')}]':
            if len(stack) >= 1:
                x = stack.pop()
            else:
                return False
            if x == '(' and i != ')':
                return False
            elif x == '[' and i != ']':
                return False
            elif x == '{' and i != '}':
                return False

    return True
#print validateBracket('[((()))]')
#print validateBracket('[()[]()()]')
#print validateBracket('[()[{(}])))]')


def removedup(arr):
    out = list()
    for i in arr:
        if i not in out:
            out.append(i)

    return out

def qsort(arr):
    if arr == []:
        return arr

    pivot = arr[0]
    left = [ i for i in arr if i < pivot ]
    equal = [ i for i in arr if i == pivot ]
    right = [ i for i in arr if i > pivot ]
    return ''.join(qsort(left)) + ''.join(equal) + ''.join(qsort(right))







arr= 'adfjkldfjlkajfejkwnmnmzncjkqddsmfncsdmanmcfoweqoieqwureyqouyuewyeuwyiuwyeqwiuyeqouiweq;;'
print removedup(arr)
print qsort(arr)
