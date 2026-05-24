class Solution:
    def decodeString(self, s: str) -> str:
        
        numstack=[]
        charstack=[]
        num=0
        temps=""
        for c in s:
            o=ord(c)
            if 48<=o<=57:
                num=(num*10)+int(c)
            elif 97<=o<=122:
                temps+=c
            elif c =='[':
                charstack.append(temps)
                numstack.append(num)
                num=0
                temps=""
            else:
                temps=charstack.pop()+(temps*numstack.pop())
        
        return temps

