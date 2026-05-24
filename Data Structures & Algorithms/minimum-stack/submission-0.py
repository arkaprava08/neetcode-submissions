class MinStack:

    def __init__(self):
        self.modStack=[]

    def push(self, val: int) -> None:
        if self.modStack:
            prevMin,topval=self.modStack[-1].split("$")
            currMin=min(int(prevMin), val)
            self.modStack.append(f"{currMin}${val}")
        else:
            self.modStack.append(f"{val}${val}")
        

    def pop(self) -> None:
        return int(self.modStack.pop().split("$")[1])
        

    def top(self) -> int:
        return int(self.modStack[-1].split("$")[1])
        

    def getMin(self) -> int:
        return int(self.modStack[-1].split("$")[0])
        
