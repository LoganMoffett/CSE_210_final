class Linked_list:
    class Node:
        
        def __init__(self, data):
            """
            create a subclass to hold the information to be stored in the linked_list
            """
            self.data = data
            self.next = None
            self.prev = None
    
    def __init__(self):
        """
        The linked list will start out empty
        """
        self.head = None
        self.tail = None

    def insert_head(self, data):
        """
        This will add the head into the linked list
        """
        new_node = Linked_list.Node(data)
        #If a head does not already exist, create a new head.
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        #If the head does exist, then make a new head
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_tail(self, data):
        """
        Add a tail into the linked_list
        """
        new_node = Linked_list.Node(data)
        #If the tail does not already exist, make one
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_after(self, old_data, data):
        """
        This is the guts of the linked list, it will add data into the middle of the linked list.
        """
        new_node = Linked_list.Node(data)
        curr = self.head
        while curr is not None:
            if curr.data == old_data:
                #If curr is the tail, then we will need to insert a new tail
                if curr == self.tail:
                    self.insert_tail(data)
                else:
                    new_node.next = curr.next
                    new_node.prev = curr
                    curr.next.prev = new_node
                    curr.next = new_node
                return
            else: 
                curr = curr.next
    
    def insert_before(self, old_value, data):
        pass

    def is_in(self, value):
        pass

    def remove(self, value):
        pass
        
        

