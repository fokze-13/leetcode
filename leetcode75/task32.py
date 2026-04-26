from collections import deque

class RecentCounter:

    def __init__(self):
        self.requests = deque()
        self.counter = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        self.counter += 1

        while t - self.requests[0] > 3000:
            self.requests.popleft()
            self.counter -= 1

        return self.counter
