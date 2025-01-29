class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        uzunluk = min(len(str1), len(str2))

        for i in range(uzunluk, 0, -1):  
            substr = str1[:i]  

            if str1 == substr * (len(str1) // i) and str2 == substr * (len(str2) // i):
                return substr  
        
        return ""
