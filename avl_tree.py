"""
CSE212 
(c) BYU-Idaho
09-Prove - Problems

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

class BST:
    """
    Implement the Binary Search Tree (BST) data structure.  The Node 
    class below is an inner class.  An inner class means that its real 
    name is related to the outer class.  To create a Node object, we will 
    need to specify BST.Node
    """

    class Node:
        """
        Each node of the BST will have data and links to the 
        left and right sub-tree. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
       
            self.data = data
            self.left = None
            self.right = None
            self.prev = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def insert(self, data):
        """
        Insert 'data' into the BST.  If the BST
        is empty, then set the root equal to the new 
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    ###################
    # Start Problem 1 #
    ###################
    def _insert(self, data, node):
        """
        This function will look for a place to insert a node
        with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
                node.left.prev = node
                self._is_balanced(node)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        #If we find the data inside of a node, then instead of inserting it just end the insert function.
        elif data == node.data:
            return
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
                node.right.prev = node
                self._is_balanced(node)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)


    
    #################
    # End Problem 1 #
    #################

    def __contains__(self, data):
        """ 
        Checks if data is in the BST.  This function
        supports the ability to use the 'in' keyword:

        if 5 in my_bst:
            ("5 is in the bst")

        """
        return self._contains(data, self.root)  # Start at the root

    ###################
    # Start Problem 2 #
    ###################
    def _contains(self, data, node):
        """
        This function will search for a node that contains
        'data'.  The current sub-tree being search is 
        represented by 'node'.  This function is intended
        to be called the first time by the __contains__ function.
        """
        #If data is the same as the data in the node, then we do have it already stored.
        if data == node.data:
            return True
        #This is just the same navigation code as searching through the data.
        elif data < node.data:
            if node.left is None:
                return False
            else:
                return self._contains(data, node.left)
        else:
            if node.right is None:
                return False
            else:
                return self._contains(data, node.right)



    #################
    # End Problem 2 #
    #################

    def __iter__(self):
        """
        Perform a forward traversal (in order traversal) starting from 
	    the root of the BST.  This is called a generator function.
        This function is called when a loop	is performed:

        for value in my_bst:
            print(value)

        """
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
        """
        Does a forward traversal (in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the left
        side (thus getting the smaller numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the right side (thus getting the larger numbers last).

        The use of the 'yield' will allow this function to support loops
        like:

        for value in my_bst:
            print(value)

        The keyword 'yield' will return the value for the 'for' loop to
	    use.  When the 'for' loop wants to get the next value, the code in
	    this function will start back up where the last 'yield' returned a 
	    value.  The keyword 'yield from' is used when our generator function
        needs to call another function for which a `yield` will be called.  
        In other words, the `yield` is delegated by the generator function
        to another function.

        This function is intended to be called the first time by 
        the __iter__ function.
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        
    def __reversed__(self):
        """
        Perform a formward traversal (in order traversal) starting from 
        the root of the BST.  This function is called when a the 
        reversed function is called and is frequently used with a for
        loop.

        for value in reversed(my_bst):
            print(value)

        """        
        yield from self._traverse_backward(self.root)  # Start at the root

    ###################
    # Start Problem 3 #
    ###################
    def _traverse_backward(self, node):
        """
        Does a backwards traversal (reverse in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the right
        side (thus getting the larger numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the left side (thus getting the smaller numbers last).

        This function is intended to be called the first time by 
        the __reversed__ function.        
        """
        #This is just traverse_forward but in reverse.
        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)

    #################
    # End Problem 3 #
    #################

    def get_height(self):
        """
        Determine the height of the BST.  Note that an empty tree
        will have a height of 0 and a tree with one item (root) will
        have a height of 1.
        
        If the tree is empty, then return 0.  Otherwise, call 
        _get_height on the root which will recursively determine the 
        height of the tree.
        """
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  # Start at the root

    ###################
    # Start Problem 4 #
    ###################
    def _get_height(self, node, count = 1):
        """
        Determine the height of the BST.  The height of a sub-tree 
        (represented by 'node') is 1 plus the height of either the 
        left sub-tree or the right sub-tree (whichever one is bigger).

        This function intended to be called the first time by 
        get_height.
        """
        #This first test will see if everything is empty below it and if so then we have hit the end of the tree
        if node.right is None:
            if node.left is None:
                return count
            #If node.right is empty but node.left is not, then keep counting node.left
            else:
                return self._get_height(node.left, count + 1)
        #If node.right is not empty but node.left is, then keep going down node.right side for count
        elif node.left is None:
            return self._get_height(node.right, count + 1)
        #If both sides have something in it then check which side is greater and return that count.
        else:
            if self._get_height(node.right, count + 1) > self._get_height(node.left, count + 1):
                return self._get_height(node.right, count + 1)
            else:
                return self._get_height(node.left, count + 1)
    
    def _is_balanced(self, node):
        #############################################################
        # if it is going to return false, we want to rotate the tree
        # Remove the return False statments so that it will rotate
        #############################################################
        if node is None:
            return True
        elif node.right is None:
            if node.left is None:
                return True
            elif self._get_height(node.left) > 1:
                return False
            else:
                return True
        elif node.left is None:
            if self._get_height(node.right) > 1:
                return False
        len_1 = self._get_height(node.right)
        len_2 = self._get_height(node.left)
        #if (len_1 - len_2) > 1:
        print('enter')
        self.rotate_right(node)
        self.is_balanced(node)

    def is_balanced(self):
        if self.root is None:
            return True
        elif self.root.right is None:
            if self.root.left is None:
                return True
            elif self._get_height(self.root.left) > 1:
                return False
            else:
                return True
        elif self.root.left is None:
            if self._get_height(self.root.right) > 1:
                return False
        len_1 = self._get_height(self.root.right)
        len_2 = self._get_height(self.root.left)
        if (len_1 - len_2) > 1 or (len_1 - len_2) < 0:
            return False
        return True


        

    def rotate_right(self, node):
        node.right.prev = node.prev
        node.prev = node.right
        if node.left is not None:
            node.right.left = node.left
        node.right.right = node
        node.right = None
        

    #################
    # End Problem 4 #
    #################


# NOTE: Functions below are not part of the BST class above. 

def create_bst_from_sorted_list(sorted_list):
    """
    Given a sorted list (sorted_list), create a balanced BST.  If 
    the values in the sorted_list were inserted in order from left
    to right into the BST, then it would resemble a linked list (unbalanced). 
    To get a balanced BST, the _insert_middle function is called to 
    find the middle item in the list to add first to the BST.  The 
    _insert_middle function takes the whole list but also takes a 
    range (first to last) to consider.  For the first call, the full 
    range of 0 to len()-1 used.
    """
    bst = BST()  # Create an empty BST to start with 
    _insert_middle(sorted_list, 0, len(sorted_list)-1, bst)
    return bst

###################
# Start Problem 5 #
###################
def _insert_middle(sorted_list, first, last, bst, last_middle = 0):
    """
    This function will attempt to insert the item in the middle
    of 'sorted_list' into the 'bst' tree.  The middle is 
    determined by using indicies represented by 'first' and 'last'.
    For example, if the function was called on:

    sorted_list = [10, 20, 30, 40, 50, 60]
    first = 0
    last = 5

    then the value 30 (index 2 which is the middle) would be added 
    to the 'bst' (the insert function above can be used to do this).   

    Subsequent recursive calls are made to insert the middle from the values 
    before 30 and the values after 30.  If done correctly, the order
    in which values are added (which results in a balanced bst) will be:

    30, 10, 20, 50, 40, 60

    This function is intended to be called the first time by 
    create_bst_from_sorted_list.

    The purpose for having the first and last parameters is so that we do 
    not need to create new sublists when we make recursive calls.  Avoid 
    using list slicing to create sublists to solve this problem.

    """
    #create bst as a BST class so that it will create a BST
    if bst is None:
        bst = BST()
    #Special case where there is nothing put in.
    if len(sorted_list) == 0:
        return
    #middle serves as the index
    middle = (first + last) // 2
    #End case. once first is greater then last, we are dealing with duplicats.
    if first > last:
        return
    else:
        #insert the node
        bst.insert(sorted_list[middle])
        #continue building the tree by going on both subbranches from the root.
        _insert_middle(sorted_list, first, middle - 1, bst)
        _insert_middle(sorted_list, middle + 1, last, bst)




#################
# End Problem 5 #
#################


# Sample Test Cases (may not be comprehensive) 
print("\n=========== PROBLEM 1 TESTS ===========")
tree = BST()
tree.insert(10)
tree.insert(9)
tree.insert(8)
tree.insert(7)
print(tree.is_balanced())
for item in tree:
    print(item)


