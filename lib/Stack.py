class Stack:

    def __init__(self, items = [], limit = None):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.limit is None or self.size() < self.limit:
            self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)        

    def full(self):
        if self.limit is None:
            return False
        return len(self.items) == self.limit

    def search(self, target):
        if target in self.items:
            return self.size() - 1 - self.items.index(target)
        return -1
