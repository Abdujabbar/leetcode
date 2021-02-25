class Solution:
    def validIPAddress(self, IP: str) -> str:
        def isHex(c):
            return '0' <= c <= '9' or 'a' <= c <= 'f' or 'A' <= c <= 'F'
        
        def checkIPV4(ip):
            partials = ip.split(".")
            
            if len(partials) != 4:
                return False
            
            for partial in partials:
                try:
                    if len(partial) > 1 and partial[0] == '0' or int(partial) > 255:
                        return False
                except Exception:
                    return False
            
            return True
        
        
        def checkIPV6(ip):
            partials = ip.split(':')
            if len(partials) != 8:
                return False
            
            for partial in partials:
                if len(partial) == 0 or len(partial) > 4:
                    return False
                
                for c in partial:
                    if not isHex(c):
                        return False
                        
            return True
        
        if checkIPV4(IP):
            return "IPv4"
        
        if checkIPV6(IP):
            return "IPv6"
        
        return "Neither"