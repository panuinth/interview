"""

1. Reverse each words in the string. Dont use string reverse function
input:
Hello how Are you
output:
olleH woh erA uoy
"""

def reverseString(s):
    out = list()
    for i in s:
        out.insert(0, i)
    return ''.join(out)

print reverseString('Hello how Are you')



def sqroot(i, prec):
    # @i : sqroot value
    # @prec: 0.01
    first = 0.0
    last = i
    med = (first + last) / 2
    while abs(( med * med ) - i) > prec:
        if ( med * med ) < i:
            first = med
        else:
            last = med
        med = ( first + last ) / 2

    if round(med) * round(med) == i:
        return round(med)
    return med

print sqroot(49, 0.000001)


print """
Return the minimal number of bills need to pay this N dollars
"""

def billsOfNum(num):
    bills_no = 0
    bills = [100, 50, 20, 10, 5, 2, 1]
    for i in bills:
        print num/ i
        if num / i > 0:
            bills_no += num/i
            tmp = (num/i) * i
            num -= tmp
            print "Bill {0} * {1} remaining = {2}".format(i, tmp, num)
    return bills_no

print billsOfNum(804)

