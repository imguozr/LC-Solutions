class Solution:
    """
        Store all digits by the mod of 3.
        Calculate the sum of all digits.
        If sum == 0:
            return '0'
        If sum mod 3 == 0 :
            Add mod1 and mod2 to mod0.
        If sum mod 3 == 1:
            If mod1 has more than 1 item:
                Pop 1 item.
            Else:
                If mod2 has more than 2 items:
                    Pop 2 item.
            Add mod1 and mod2 to mod0.
        If sum mod 3 == 2:
            If mod2 has more than 1 item:
                Pop 1 item.
            Else:
                If mod1 has more than 2 items:
                    Pop 2 items.
            Add mod1 and mod2 to mod0.
        Sort mod0.
        Return string.
    """

    def largestMultipleOfThree(self, digits):
        res, mod_1, mod_2 = [], [], []
        for d in digits:
            if not d % 3:
                res.append(d)
            elif d % 3 == 1:
                mod_1.append(d)
            else:
                mod_2.append(d)

        d_sum = sum(digits)
        if not d_sum:
            return '0'
        if not d_sum % 3:
            res += mod_1 + mod_2
        elif d_sum % 3 == 1:
            if mod_1:
                mod_1.sort(reverse=True)
                mod_1.pop()
            else:
                if len(mod_2) >= 2:
                    mod_2.sort(reverse=True)
                    mod_2.pop()
                    mod_2.pop()
            res += mod_1 + mod_2
        else:
            if mod_2:
                mod_2.sort(reverse=True)
                mod_2.pop()
            else:
                if len(mod_1) >= 2:
                    mod_1.sort(reverse=True)
                    mod_1.pop()
                    mod_1.pop()
            res += mod_1 + mod_2
        res.sort(reverse=True)
        return ''.join(map(str, res))
