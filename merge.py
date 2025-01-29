class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1=len(word1)
        len2=len(word2)
        output=[]
        if 1<= len(word1) and len(word2) <=100 :
            for i in range(min(len1, len2)):
                output.append(word1[i])
                output.append(word2[i])
            if len(word1) > len(word2):
                output.append(word1[min(len1,len2):])
            else:
                output.append(word2[min(len1,len2):])

                
            result = ''.join(output)
            return result

        
