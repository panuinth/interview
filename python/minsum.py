
def minsum(n, arr=[1,2,3,4,5]):
    arr = sorted(arr, reverse=True)
    out = []
    for i in arr:
        n -= i
        out.append(i)
        if n<0:
            return out
    return False

def minadjsum(n, arr=[2,1,1,4,3,6]):
    #sliding windows
    for size in range(len(arr)):
        for index in range(len(arr)):
            if sum(arr[index:index+size]) >= n:
                return arr[index:index+size]
    return False
print minadjsum(10)


#def nexthighnum(n):
    #"""
        #sort input asc
        #54321
        #67285 = 67582


        #12345 search for
    #"""
    ##size
    #for i in range(2, len(str(n))+1):
        #window = str(n)[0-i:]
        ##position
        #for x in range(2, len(window)):
            #if window[-1-i] < window[-1]:
                #return str(n)[:len(str(n)-len(window))] +

#print nexthighnum(67285)



def strcompress(s="FOOOFFFF FIGHTER"):
    prv = None
    counter = 1
    for i in range(1, len(s)+1):
        print s[-i], prv, counter
        if s[-i] != prv:
            prv = s[-i]
            if counter >= 3:
                print 'xx'
                s = s[:1-i+1]+str(counter)+s[1-i+counter:]
            counter = 1
        else:
            counter += 1
    return s

print strcompress()

