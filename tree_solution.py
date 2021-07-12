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

class Interface:

    def __init__(self, tree):
        """
        initializes the interface so that we can interact with the multibranch treen
        """
        self.tree = tree
        self.data = None
        self.child = None
        self.branch = None

    def display(self):
        if self.branch == None:
            print(f"Parant {self.tree.root.data}")
            for child in self.tree.root.children:
                print(f"child {child.data}")
            print()
        else:
            print(f"Parant {self.branch.data}")
            for child in self.branch.children:
                print(f"child {child.data}")
            print()

    def nav(self, option):
        if self.branch is None:
            self.branch = self.tree.root
        if option == 'b':
            self.branch = self.branch.parent
        else:
            self.branch = self.branch.children[option - 1]

        

tree = Tree()
interface = Interface(tree)
tree.insert_root(1)
tree.insert_child(1, 2)
tree.insert_child(1, 3)
tree.insert_child(2, 4)
tree.insert_child(3, 10)
tree.insert_child(10, 5)
tree.insert_child(1, 5)
interface.display()
interface.nav(1)
interface.display()
interface.nav('b')
interface.display()
interface.nav(2)
interface.display()
interface.nav(1)
interface.display()