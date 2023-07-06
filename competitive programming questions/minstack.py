class MinStack:
    def __init__(self):
        self.lst = []
        self.min = None
        
    def push(self, val: int) -> None:
        self.lst.append(val)
        if self.min == None or val < self.min:
            self.min = val        

    def pop(self) -> None:
        if not self.lst: return None
        else: return self.lst.pop()

    def top(self) -> int:
        if not self.lst: return None
        else: return self.lst[-1]
        
    def getMin(self) -> int:
        if self.min == None: return None 
        else: return self.min