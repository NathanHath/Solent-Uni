from stack import Stack
stack1 = Stack()
stack1.push(1)
stack1.push(4)
stack1.push(9)

print(stack1.pop())
print(stack1)

stack2 = Stack()
stack2.push("Linux")
stack2.push("windows")
stack2.push("Mac OS")
try:
    print(stack2.pop())
    print(stack2.pop())
    print(stack2.pop())
    print(stack2.pop())
except Exception as e:
    print(f"ERROR: {e}")    