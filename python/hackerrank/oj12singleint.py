class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        A = sorted(A)
        for i in range((len(A)/2)+1):
            if i == len(A)/2:
                return A[i*2]
            elif A[i*2] != A[(i*2)+1]:
                return A[i*2]
        return None


def test():
    A = [ i for i in range(100)] + [ i for i in range(100)]
    A.append(1022)
    print len(A)
    print Solution().singleNumber(A)
            
def test1():
    A = [-1]
    print Solution().singleNumber(A)

test1()
