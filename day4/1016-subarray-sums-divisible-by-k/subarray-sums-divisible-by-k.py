class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
            cum_mod = []
            sum = 0

            for x in nums:
                sum += x
                cum_mod.append(sum % k)

            mod_dict = Counter(cum_mod)
            
            res = 0
            for i in mod_dict:
                if i == 0:
                    res += mod_dict[i]
                if mod_dict[i] > 1:
                    res += int(mod_dict[i] * (mod_dict[i] - 1) / 2)
                
            return res