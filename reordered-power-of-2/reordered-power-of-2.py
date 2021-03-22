from collections import Counter
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        power = 1
        cnt = Counter(str(N))
        while power < 10 ** 9:
            ccn_power = Counter(str(power))
            if ccn_power == cnt:
                return True
            power *= 2
        
        return False