class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""
    
        for i in range(len(palindrome)//2 + 1):
            if palindrome[i] != "a":
                ans = palindrome[:i] + "a" + palindrome[i + 1:]
                if ans != ans[::-1]:
                    return ans
        
        return palindrome[:len(palindrome) - 1] + "b"