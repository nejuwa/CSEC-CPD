class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        zero = [0] * (len(s)+1)
        for shift in shifts:
            if shift[2] == 0:
                zero[shift[0]] -=1
                zero[shift[1]+1] +=1

            if shift[2] == 1:
                zero[shift[0]] +=1
                zero[shift[1]+1] -=1
        
        for i in range(1,len(s)):
            zero[i] += zero[i-1]
        
        ans = []
        for i in range(len(s)): 
            zzz = ( zero[i]+ ord(s[i]) - ord('a')) %26 + ord('a')
            ans.append(chr(zzz))
        return ''.join(ans)
        
        


      
