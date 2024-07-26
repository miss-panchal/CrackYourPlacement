class Solution:
    def romanToInt(self, s: str) -> int:
        # Mapping of Roman numerals to their integer values
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans = 0
        n = len(s)
        
        for i in range(n):
            # If the current value is less than the next value, subtract it
            if i + 1 < n and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                ans -= roman_to_int[s[i]]
            else:
                ans += roman_to_int[s[i]]
        
        return ans
