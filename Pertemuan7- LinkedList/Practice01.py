class node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = node('a')
b = node('b')
c = node('c')

a.next = b
b.next = c

current = a 
while current:
    print(f'Node @{id(current)} | Data :{current.data}, | Next: {id(current.next) if current.next else None}')
    current = current.next

    
