class Node:
    def __init__(self, data):
        """
        Create a Node object with the data specified. self.next is set to None by default
        :param data: the data to be stored in the node
        """
        self._data = data
        self._next = None

    def set_next(self, next_node):
        """
        Sets the current Node to point at the specified Node object
        :param Node next_node: the node to point at
        :return: None
        """
        self._next = next_node

    def get_next(self):
        """
        Returns the Node object which the current node is pointing at
        :return: the next Node in the linked list
        """
        return self._next

    def get_data(self):
        """
        Returns the data stored in the current Node
        :return: the data stored in the current Node
        """
        return self._data


class LinkedList:
    def __init__(self):
        """
        creates a new linked list object with two class variables, self.head (the first item in the list, default=None),
        and self.length (the length of the list, default=0)
        """
        self._head = None
        self._length = 0

    def _calc_length(self):
        """
        Traverses the entire linked list in order to calculate its length and then sets the self.length class variable
        :return:
        """
        # First check if self.head exists - if it doesn't, self.length is 0, if it does self.length will need to be
        # calculated. Create a count variable to keep track of how many nodes you've passed (start at 1). set temp to
        # self.head, then loop through until temp.get_next() is None, adding one onto your count and reassigning temp to
        # temp.get_next(). Once calculated, set self.length to count.
        if self._head is None:
            self._length = 0

        length = 1
        current_node = self._head
        while current_node.get_next() is not None:
            current_node = current_node.get_next()
            length += 1
        self._length = length

    def traverse(self, stop=-1):
        """
        Traverses the linked list up to the index specified, or to the end of the list if no index is specified
        :param stop: the index to traverse the list up to before returning the Node
        :return: the Node object which exists at the specified index
        """
        # Similar to the calc_length method above. set temp to self.head. Now traverse through the list (you know the
        # length of the list so you can use a for loop here. At each stage in the loop, if temp.get_next() is None or
        # i = stop (assuming you used i as your iteration variable), return temp. Otherwise, set temp to equal
        # temp.get_next()
        if self._length < stop:
            raise IndexError("Out of index.")

        node = self._head
        if stop == -1:
            while node.get_next() is not None:
                node = node.get_next()
        else:
            for i in range(stop):
                node = node.get_next()
        return node

    def add_at_start(self, data):
        """
        Adds a data node at the start of the linked list
        :param data: The data to be stored
        :return: None
        """
        # instantiate a new Node object, called node, with the specified data. set_next on this new node to point at the
        # head. Now set the new node as the head. Finally, calculate the length of the list.
        node = Node(data)
        node.set_next(self._head)
        self._head = node
        self._calc_length()

    def add_at_end(self, data):
        """
        Adds a data node at the end of the linked list
        :param data: The data to be stored
        :return: None
        """
        # instantiate a new Node object, called node, with the specified data. Traverse the list all the way to the
        # final node, and set_next on this node to point at the new node. Finally, calculate the length of the list
        node = Node(data)
        final_node = self.traverse()
        final_node.set_next(node)
        self._calc_length()

    def add_after(self, index, data):
        """
        Adds a data node after the specified index in the linked list
        :param int index: The index of the linked list after which to add the new node
        :param data: The data to be stored
        :return: None
        """
        # instantiate a new Node object, called node, with the specified data. Traverse the list up to the specified
        # index and store the returned object as temp. set_next on the new node to point at temp.get_next() and set_next
        # on temp to point at the new node. Finally, calculate the length of the list
        before_node = self.traverse(index)
        after_node = before_node.get_next()
        node = Node(data)
        node.set_next(after_node)
        before_node.set_next(node)
        self._calc_length()

    def add_before(self, index, data):
        """
        Adds a data node before the specified index in the linked list
        :param int index: the index of the node before which the new node will be added
        :param data: The data to be stored
        :return: None
        """
        # If the index is 0, call self.add_at_start(data). Otherwise, do the following: instantiate a new node with the
        # data specified. Traverse the list up to the specified index-1 and store the returned object as temp. set_next
        # on the new node to point at temp.get_next(). set_next on temp to point at the new node. Finally, calculate the
        # length of the list
        if index == 0:
            self.add_at_start(data)
        else:
            node = Node(data)
            before_node = self.traverse(index - 1)
            node.set_next(before_node.get_next())
            before_node.set_next(node)
        self._calc_length()

    def del_from_start(self):
        """
        Removes a node from the start of the list
        :return: None
        """
        # set head to head.get_next(). Now calculate the length of the list
        self._head = self._head.get_next()

    def del_from_end(self):
        """
        Removes a node from the end of the list
        :return: None
        """
        # if length is 1, call self.del_from_start. Otherwise, so the following: Traverse the list up to length-2 and
        # set_next on the returned object to point at None. Finally, calculate the length of the list.
        if self._length == 1:
            self.del_from_start()
        else:
            self.traverse(self._length - 2).set_next(Node)
        self._calc_length()

    def del_after(self, index):
        """
        Deletes the Node after the specified index
        :param int index: the index after which the node should be deleted
        :return:
        """
        # If index is one less than length, call self.del_from_end(). Otherwise, do the following: traverse the list up
        # to the specified index and store the returned object as temp. Now traverse up to index+1 and call get_next()
        # on the returned object. set_next on temp to be whatever the result of this get_next is. Finally, calculate the
        # length of the list
        if index - 1 == self._length:
            self.del_from_end()
        else:
            before_node = self.traverse(index)
            del_node = before_node.get_next()
            before_node.set_next(del_node.get_next())
            # Lil bit of verboseness
            del del_node

    def del_before(self, index):
        """
        Deletes the Node before the specified index
        :param int index: the index before which the Node will be deleted
        :return: None
        """
        # if index = 1, call self.del_from_start(). Otherwise, do the following: Traverse the list up to the specified
        # index and store the returned object as temp. traverse the list up to index-2 and set_next on the returned
        # object to temp. Finally, calculate the length of the list

    def __str__(self):
        return "Linked List: " + " -> ".join([self.traverse(i).get_data() for i in range(self.length)])
