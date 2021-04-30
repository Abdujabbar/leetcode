class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniques = set()
        
        for email in emails:
            partials = email.split('@')
            username = partials[0]
            valid_username = ""
            for c in username:
                if c == '+':
                    break
                if 'a' <= c <= 'z':
                    valid_username += c
            
            uniques.add(valid_username + '@' + partials[1])
        
        return len(uniques)