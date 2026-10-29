class linkedlist:
    def __init__(self):
        self.first = None
        self.last = None
        self.prev = None
        self.size = 0

    def add(self, node):
        if self.first == None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.prev = self.last
            self.last = node
        self.size += 1

    def get(self,index):
        current = self.first
        if index >= self.size // 2:
            # range(self.size - 1, index, -1)
            for i in range(index):
                if current == None:
                    raise IndexError("Index out of range")
                else:
                    current = current.next

        elif self.size > index:
            for i in range(self.size - 1, index, -1):
                if current == None:
                    raise IndexError("Index out of range")
                else:
                    current = current.next

        return current

    def __str__ (self):
        return self.first.__str__()



