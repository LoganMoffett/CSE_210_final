class Tree:
    class Node:
        
        def __init__(self, data):
            self.data = data
            self.parent = None
            self.children = []

        def add_child(self, child, parent):
            child.parent = parent
            self.children.append(child)

        def get_children(self):
            return self.children

    def __init__(self):
        self.root = None

    def insert_root(self, data):
        new_node = Tree.Node(data)
        self.root = new_node

    def insert_child(self, parent, child):
        curr = self.root
        node = Tree.Node(child)
        if curr.data == parent:
            curr.add_child(node, curr)
        else:
            self._insert_child(parent, node, curr)
             
    def _insert_child(self, parent, child, curr):
        if curr is None:
            return False
        elif curr.data == parent:
            curr.add_child(child, curr)
            return True
        else:
            for x in range(0, len(curr.get_children())):
                if self._insert_child(parent, child, curr.children[x]) == True:
                    return True

class Binary_Tree:
    class Node:
        
        def __init__(self, data):
            self.data = data
            self.right = None
            self.left = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Binary_Tree.Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, curr):
        if data < curr.data:
            if curr.left is None:
                curr.left = Binary_Tree.Node(data)
            else:
                self._insert(data, curr.left)
        else:
            if curr.right is None:
                curr.right = Binary_Tree.Node(data)
            else:
                self._insert(data, curr.right)

        

tree = Tree()
tree.insert_root(1)
tree.insert_child(1, 2)
tree.insert_child(1, 3)
tree.insert_child(2, 10)
tree.insert_child(3, 10)
interface = Interface(tree)
interface.display()
interface.nav(1)
interface.display()
interface.nav('b')
interface.display()
interface.nav(2)
interface.display()