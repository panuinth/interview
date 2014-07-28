class Solution:
    # @param s, a string
    # @return a string
    # tc1: "cat dog monkey"
    # tc2: "hello world "
    # tc3: " there  is  two  spaces"
    def reverseWords(self, s):
        out = []
        tmp = ""
        for i in range(len(s)):
            if s[i] == " ":
                if tmp:
                    out.insert(0, tmp)
                    tmp = ""
            elif i == len(s)-1:
                tmp += s[i]
                out.insert(0, tmp)
                tmp = ""
            else:
                tmp += s[i]

        return " ".join(out)


def testA():
    string = "cat dog monkey"
    print Solution().reverseWords(string)

def testSet():
    arr = [ " a b c de fgh",
            "  abc  def",
            "abc",
            "a",
            " 1",
            "1 ",
            "   a   b "]
    for i in arr:
        print Solution().reverseWords(i)
testA()
testSet()
