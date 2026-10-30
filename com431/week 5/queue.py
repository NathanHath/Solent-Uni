class Queue:
    def __init__(self, capacity):
        self.internal_array = [None] * capacity
        self.front = 0
        self.back = 0
        self.size = 0

    def add(self, item):
        if self.size < len(self.internal_array):
            self.internal_array[self.back] = item
            self.back += 1
            if self.back == len(self.internal_array):
                self.back = 0

            self.size += 1
        else:
            raise Exception('Queue is full')


    def remove(self):
        self.internal_array[self.front] = None
        self.front += 1
        if self.front == len(self.internal_array):
            self.front = 0

        self.size -= 1
    def __str__(self):
        return str(self.internal_array)
