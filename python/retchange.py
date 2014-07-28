class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        if n == 0:
            return
        if m == 0:
            A += B
            return

        mi = ni = 0




def test():
    A = [4]
    B = [1,2,3,5,6]
    Solution().merge(A, len(A), B, len(B))
    print A
test()
