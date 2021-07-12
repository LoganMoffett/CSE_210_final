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
