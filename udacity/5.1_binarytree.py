class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, start, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        if start.value == find_val:
            return True
        if start.left:
            return self.search(start.left, find_val)
        if start.right:
            return self.search(start.right, find_val)
        return False

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.preorder_print(self.root, [])

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        traversal.append(start.value)
        if start.left:
            self.preorder_print(start.left, traversal)
        if start.right:
            self.preorder_print(start.right, traversal)
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print tree.search(tree.root, 4)
# Should be False
print tree.search(tree.root, 6)

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree()