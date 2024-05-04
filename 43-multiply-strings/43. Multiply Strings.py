class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        num1 = num1[::-1]
        num2 = num2[::-1]
        n1 = len(num1)
        n2 = len(num2)
        res = 0
        for i in range(n2):
            carry = 0
            summ = 0
            for j in range(n1):
                prod = int(num2[i])*int(num1[j]) + carry
                carry = prod // 10
                mod = prod % 10
                summ += mod*(10**j)
            summ += carry*(10**(n1))
            res += summ*(10**i)
        return str(res)
