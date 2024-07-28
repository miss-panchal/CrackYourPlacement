class Solution:
    def reverseWords(self, s: str) -> str:
        
        a= s.split()
        b=(a[::-1])

        reversed_string = ' '.join(b)
        return reversed_string