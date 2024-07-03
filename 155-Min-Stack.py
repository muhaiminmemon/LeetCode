class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            if val <= self.min_stack[-1]:
                self.min_stack.append(val)

    def pop(self) -> None:
        if len(self.stack) > 0:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        if len(self.min_stack) > 0:
            return self.min_stack[-1]
        else:
            return None