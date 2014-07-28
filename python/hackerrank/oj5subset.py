class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, s):
        if not s:
            return s
        print s
        for i in range(len(s)):
            tmp = s
            print i
            print 'tmp=', tmp
            print 's=', s
            tmp.pop(i)

            self.subsetsWithDup(tmp)

def test():
    Solution().subsetsWithDup([1,2,2])

test()
