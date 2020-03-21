class Solution:
    """
        Multiplication of two strings
        Applicable to multiplication of two big numbers
    """

    def multiply1(self, num1: str, num2: str) -> str:
        """
            Simulate multiply by hand
        """
        if num1 == '0' or num2 == '0':
            return '0'

        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            carry = 0
            for j in range(n - 1, -1, -1):
                tmp = int(num1[i]) * int(num2[j]) + carry
                carry, res[i + j + 1] = divmod(res[i + j + 1] + tmp, 10)
            res[i] += carry
        return ''.join(map(str, res)).lstrip('0')

    def multiply2(self, num1: str, num2: str) -> str:
        """
            Use Karatsuba Algorithm
            half = max(len1 + len2) // 2
            x = 10 ** half * a + b
            y = 10 ** half * c + d
            x * y = 10 ** (2 * half) * ac + 10 ** half * (ad + bc) + bd
        """
        def karatsuba(n1, n2):
            if n1 < 10 or n2 < 10:
                return n1 * n2

            m, n = len(str(n1)), len(str(n2))
            half = max(m, n) // 2

            a, b = divmod(n1, 10 ** half)
            c, d = divmod(n2, 10 ** half)

            z0 = karatsuba(a, c)
            z1 = karatsuba(b, d)
            z2 = karatsuba(a + b, c + d) - z0 - z1

            return z0 * 10 ** (2 * half) + z2 * 10 ** half + z1

        return str(karatsuba(int(num1), int(num2)))
