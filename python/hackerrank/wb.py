def reverseString2(s):
    first = 0
    last = len(s) - 1
    s = list(s)
    while first < last:
        x, y = s[first], s[last]
        s[first] = y
        s[last] = x
        first += 1
        last -= 1
    return s


def test_1():
    print reverseString2('Hello World')
    print reverseString2('Hello! World')

#test_1()

def reverseWords(s):
    if type(s) != type('s'):
        return False
    s = s.split(' ')
    s = s[::-1]
    return ' '.join(s)




def test_2():
    print reverseWords('Hello! World')
    print reverseWords('')
    print reverseWords(0)
    print reverseWords(None)


#test_2()


class netString:
    def serialization(self, arr):
        # @input    arr: array of string
        # @return   out: serialized string
        out = ''
        for i in arr:
            out += "{0},{1}".format(len(i), i)
        return out

    def deserialization(self, s):
        # @input is serialized string
        # @return array of string
        i = 0
        eom = -1
        out = list()
        while i < len(s):
            if s[i] == ',':
                print eom, i, s[eom+1:i]
                msg_len = int(s[eom+1:i])

                out.append(s[i+1:i+1+msg_len])
                i += msg_len
                eom = i
            else:
                i += 1
            print out
        return out

def test_netstring():
    s = netString().serialization(["abcdef", 'erqewwfdsaf', "!@#SAFSA"])
    print s
    arr = netString().deserialization(s)
    print arr

test_netstring()



def mergeSortedList(arr1, arr2):
    l1 = len(arr1)
    l2 = len(arr2)
    i = j = 0
    out = list()
    while i < l1 and j < l2:
        if arr1[i] < arr2[j]:
            out.append(arr1[i])
            i += 1
        else:
            out.append(arr2[j])
            j += 1
    while i < l1:
        out.append(arr1[i])
        i += 1
    while j < l2:
        out.append(arr2[j])
        j += 1

    return out

def test_merge_sorted_list():
    arr1 = [1,2,3,444,666,777,98888, 1231232131]
    arr2 = [1,2,3,4,5,6,7,8,9, 10]
    print mergeSortedList(arr1, arr2)
    print mergeSortedList(arr1, [])
    print mergeSortedList([], arr2)
    print mergeSortedList([], [])

test_merge_sorted_list()



def reverseDp(s):
    if s:
        print s[-1]
        reverseDp(s[:-1])
    else:
        return

def test_reverse_dp():
    reverseDp('abcdefghijklmnopqrstuvwxyz')

#test_reverse_dp()





def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

def is_substr(find, data):
    print find
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True

print '*' * 10

print long_substr(['Oh, hello, my friend.',
                   'I prefer Jelly Belly beans.',
                   'When hell freezes over!'])
