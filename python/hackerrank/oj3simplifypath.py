class Solution:
    # @param path, a string
    # @return a string
    # path /./ - current
    # path /../ - up one level
    # path /home/ -> /home
    # path /home//foo -> /home/foo
    def simplifyPath(self, path):
        arr = path.split('/')
        out = list()
        for i in arr:
            if i == '.' or i == '':
                # do nothing
                pass
            elif i == '..':
                if out:
                    out.pop()
            else:
                out.append(i)
        return '/'+'/'.join(out)


def test():
    for i in [ '/home//foo', '/home/../work/']:
        print Solution().simplifyPath(i)


test()
