class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = []
        carry = 0
        lenA = len(a) - 1
        lenB = len(b) - 1
        while lenA >= 0 or lenB >= 0 or carry:
            if lenA >= 0:
                carry += int(a[lenA])
                lenA -= 1
            if lenB >= 0:
                carry += int(b[lenB])
                lenB -=1
            s.append(str(carry%2))
            carry //= 2
        return ''.join(reversed(s))
