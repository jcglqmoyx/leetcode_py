class MyStack:
    def __init__(self):
        self.stk = []

    def push(self, x: int) -> None:
        self.stk.append(x)
        n = len(self.stk)
        for i in range(n - 1):
            self.stk.append(self.stk[0])
            self.stk = self.stk[1:]

    def pop(self) -> int:
        return self.stk.pop(0)

    def top(self) -> int:
        return self.stk[0]

    def empty(self) -> bool:
        return not self.stk
