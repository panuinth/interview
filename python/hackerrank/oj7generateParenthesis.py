"""
n = 1 : ["()"]
n = 2 : ["(())",                "()()"]
n = 3 : ["(()())", "((()))", "(())()", "()()()", "()(())"
"""

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n, curr=[]):
        out = []
        if n == 0:
            return curr
        if not curr:
            return self.generateParenthesis(n-1, ['()'])

        for item in curr:
            for j in range(len(item)):
                new_item = item[:j]+'()'+item[j:]
                if new_item not in curr and new_item not in out:
                    out.append(new_item)
        return self.generateParenthesis(n-1, out)


def test():
    for i in range(5):
        print '******** n = {} **********'.format(i)
        print Solution().generateParenthesis(i)

test()
