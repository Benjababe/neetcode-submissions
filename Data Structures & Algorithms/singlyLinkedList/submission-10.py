class LinkedList:
    
    def __init__(self):
        self.length = 0
        self.head = None
    
    def get(self, index: int) -> int:
        if index >= self.length:
            return -1

        cur = self.head
        for _ in range(index):
            cur = cur["next"]
        return cur["val"]

    def insertHead(self, val: int) -> None:
        new_head = { "next": self.head, "val": val }
        self.head = new_head
        self.length += 1

    def insertTail(self, val: int) -> None:
        self.length += 1
        if self.head is None:
            return self.insertHead(val)
        
        cur = self.head
        while cur["next"] is not None:
            cur = cur["next"]
        cur["next"] = { "next": None, "val": val }

    def remove(self, index: int) -> bool:
        if index >= self.length:
            return False
    
        if index == 0:
            self.head = self.head["next"]
        else:
            cur = self.head
            for _ in range(index-1):
                cur = cur["next"]
            cur["next"] = cur["next"]["next"]
    
        self.length -= 1
        return True
        

    def getValues(self) -> List[int]:
        ret = []
        cur = self.head
        while cur is not None:
            print(ret, cur)
            ret.append(cur["val"])
            cur = cur["next"]
        return ret
