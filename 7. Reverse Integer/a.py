class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        s = str(x)
        if s[0] == '-':
            s = s[1:]
            s = s[::-1]
            s = s.lstrip('0')
            if not s:
                return 0
            s = '-' + s
        else:
            s = s[::-1]
            s = s.lstrip('0')
            if not s:
                return 0
        reversed_num = int(s)
        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0
        return reversed_num
