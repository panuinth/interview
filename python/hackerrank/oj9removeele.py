class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        out = list()
        A = [i for i in A if i != elem]
        return len(A)


def test():
    print Solution().removeElement([4,6,6,6,6,4,5], 6)

test()
