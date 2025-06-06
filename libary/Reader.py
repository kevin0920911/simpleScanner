class Reader:
    def __init__(self, data:str):
        self.data = data 
        self.length = len(self.data)
        self.currPos = 0
    
    def nextChar(self) -> str|None:
        if self.currPos >= self.length:
            return None
        res = self.data[self.currPos]
        self.currPos += 1
        return res
    
    def retracted(self, n:int) -> None:
        if n <= 0:
            return None
        self.currPos -= n
    
    def eof(self) -> bool:
        if self.currPos == self.length:
            return True
        return False
