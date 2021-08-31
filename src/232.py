class MyQueue:
    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)
        n = len(self.q)
        for i in range(n):
            self.q.append(self.q[0])
            self.q = self.q[1:]

    def pop(self) -> int:
        top = self.q[0]
        self.q = self.q[1:]
        return top

    def peek(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q
