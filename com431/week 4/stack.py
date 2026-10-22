class Stack:
    def __init__(self):
        self.internal_list = []

    def push(self, item):
        # Code to add an item to the stack will go here
        self.internal_list.append(item)
        pass  # ends the method when it's empty

    def pop(self):
        # Code to remove an item from the top of the stack will go here
        if len(self.internal_list) > 0:
            top_item = self.internal_list[-1]
            del self.internal_list[-1]
            return top_item
        else:
            raise Exception ("Stack is empty")

    def __str__(self):
        return self.internal_list.__str__()