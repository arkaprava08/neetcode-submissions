class Solution:
    def decodeString(self, s: str) -> str:
        
        numstack=[]
        charstack=[]
        num=0
        temps=""
        for c in s:

            if 48<=ord(c)<=57:
                num=(num*10)+int(c)
            elif 97<=ord(c)<=122:
                temps+=c
            elif c =='[':
                charstack.append(temps)
                numstack.append(num)
                print("arka: ", num, temps)
                num=0
                temps=""
            else:
                temps=charstack.pop()+(temps*numstack.pop())

        print(charstack)
        print(temps)
        # out=""
        # for char in charstack:
        #     out+=char
        
        return temps

