class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentence1 = sentence1.split(' ')
        sentence2 = sentence2.split(' ')
        
        while sentence1 and sentence2:
            if sentence2[0] == sentence1[0]:
                sentence2.pop(0)
                sentence1.pop(0)
            elif sentence2[-1] == sentence1[-1]:
                sentence2.pop()
                sentence1.pop()
            else:
                return False
        
        return True