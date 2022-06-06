from sortedcontainers import SortedDict


class MyCalendarThree:
    def __init__(self):
        self.d = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.d[start] = self.d.setdefault(start, 0) + 1
        self.d[end] = self.d.setdefault(end, 0) - 1
        res = book = 0
        for freq in self.d.values():
            book += freq
            res = max(res, book)
        return res
