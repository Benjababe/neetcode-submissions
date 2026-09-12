class MinStack:

    def __init__(self):
        self.st = []
        self.stmin = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if len(self.stmin) == 0 or val <= self.stmin[-1]:
            self.stmin.append(val)

    def pop(self) -> None:
        if self.st[-1] == self.stmin[-1]:
            self.stmin.pop()
        self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.stmin[-1]
