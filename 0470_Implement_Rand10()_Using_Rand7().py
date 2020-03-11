# The rand7() API is already defined for you.
def rand7():
    """
    :return a random integer in the range 1 to 7
    """
    pass


class Solution:
    """
        rand7() -> rand49() -> rand40() -> rand10()

        randM() -> randN() is the same.
    """
    def rand10(self) -> int:
        rand40 = 40
        while rand40 >= 40:
            rand40 = (rand7() - 1) * 7 + rand7() - 1
        return rand40 % 10 + 1
