from sortedcontainers import SortedDict


class StockPrice:
    def __init__(self):
        self.current_timestamp = -1
        self.current_price = -1
        self.pt = {}
        self.prices = SortedDict()

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.pt:
            old_price = self.pt[timestamp]
            self.prices[old_price] -= 1
            if self.prices[old_price] == 0:
                del self.prices[old_price]
        self.pt[timestamp] = price
        if price in self.prices:
            self.prices[price] += 1
        else:
            self.prices[price] = 1
        if timestamp >= self.current_timestamp:
            self.current_timestamp = timestamp
            self.current_price = price

    def current(self) -> int:
        return self.current_price

    def maximum(self) -> int:
        return self.prices.keys()[-1]

    def minimum(self) -> int:
        return self.prices.keys()[0]
