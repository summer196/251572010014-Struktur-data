class node:
    def __init__(self, data):
        self.data =  data
        self.next = None

def insert_at_beningging(head, data):
    new_node = node(data)
    new_node.next = head
    return new_node

head = node('B')
head = insert_at_beningging(head, "A")

def print_linked_list(head):
    while head:
        print(f'[{head.data}] -->', end = "")
        head = head.next
    print("NULL")

print_linked_list(head)