class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = BinaryNode("A")
root.left = BinaryNode("B")
root.right = BinaryNode("C")
root.left.left = BinaryNode("D")
root.left.right = BinaryNode("E")

def bfs_level_order(root):
    if not root:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.value, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

print("BFS Level order:")
bfs_level_order(root)