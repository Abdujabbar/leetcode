class Solution:
    def sortSentence(self, s: str) -> str:
        sequenced_dict = {}
        for w in s.split():
            num = ""
            index = len(w) - 1
            while index >= 0 and "0" <= w[index] <= "9":
                num = w[index] + num
                index -= 1
            sequenced_dict[int(num)] = w[:index + 1]
        
        res = ""
        for i in range(len(sequenced_dict)):
            res += sequenced_dict[i + 1] + " "
        
        return res.strip()