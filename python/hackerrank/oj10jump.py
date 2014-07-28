"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)"""



class Solution:
    # @param A, a list of integers
    # @return an integer
    # [2,3,1,1,4], - 2,3
    def jump(self, A, ):
        result = 0
        last = 0
        curr = 0

        for i in range(len(A)):

            if i > last:
                if curr == last and last < len(A) - 1:
                    return -1
                last = curr
                result += 1
            curr = max(curr, i+A[i])
        return result

    def jump2(self, A):
        ret = 0
        last = 0
        curr = 0
        for i in range(len(A)):
            if i > last:

                last = curr
                ret += 1
            curr = max(curr, i+A[i])
        return ret

def test():
    print Solution().jump([2,3,1,1,4])

test()
