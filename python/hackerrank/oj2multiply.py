class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def add(self, num1, num2):
        """ do one digit at a time, and carry it over to next bit
        """
        out = ""
        carry = 0
        l = len(num1) if len(num1) > len(num2) else len(num2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(l):
            tmp = 0
            x = int(num1[i]) if i + 1 <= len(num1) else 0
            y = int(num2[i]) if i + 1 <= len(num2) else 0
            tmp += x + y + carry
            carry = tmp / 10
            out = str(tmp % 10) + out
        return out

    def multiply(self, num1, num2):
        """
            do one digit at a time, and appen 0 at the end
        """
        result = list()
        for i in range(len(num1)):
            single_result = 0
            for j in range(len(num2)):
                single_result += (int(num1[i]) * int(num2[j])) * pow(10, len(num2) - 1 - j)
            result.append(str(single_result) + ('0' * (len(num1) - 1 - i)))

        out = '0'
        for i in result:
            out = self.add(out, i)
        return out

def test1(num1, num2):
    print Solution().multiply(num1, num2)

def test2(num1, num2):
    print Solution().add(num1, num2)
for i in [('13', '13'),
        ('239', '332555'),
        ("6212539488887616189474385819178920475", "3513300463458491279562464688533884446404751710059905464832688198732393780")]:
    test1(i[0], i[1])
    #test(i[0], i[1])
