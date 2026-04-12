class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.q = {}
        self.left = 0
        self.right = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.right] = value
        self.right += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.left -= 1
        self.q[self.left] = value
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.q[self.left] = None
        self.left += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.right -= 1
        self.q[self.right] = None
        return True

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.left]

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.right - 1]

    def isEmpty(self) -> bool:
        return self.left == self.right

    def isFull(self) -> bool:
        return -self.left + self.right >= self.k

m = MyCircularDeque(3)

commands = ["insertFront","getRear","insertFront","getRear","insertLast","getFront","getRear","getFront","insertLast","deleteLast","getFront"]
args = [[9],[],[9],[],[5],[],[],[],[8],[],[]]

for command, arg in zip(commands, args):
    f = m.__getattribute__(command)
    print(f"{command}({arg}) => {f(*arg)}")
    print(f"{m.q}   right={m.right}, left={m.left}")