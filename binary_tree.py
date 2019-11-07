class Node:
    def __init__(self, key, value=None, left=None, right=None):
        """
        Tree Node object
        Arguments
        --------
        key: key for node
        value: value for key
        left: left child node
        right: right child node
        --------
        """
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, key, value):
        """
        Insert root and key value pairs

        Arguments
        --------
        root: root of tree
        key, value : key and values pairs to add

        """
        if self.root is None:
            self.root = Node(key, value)
        else:
            self.add(key, value, self.root)

    def add(self, key, value, node):
        """
        Add nodes to binary tree
        Arguments
        --------
        key, value : key value pairs
        node: node to add key, value pairs

        """
        if key < node.key:
            if node.left is not None:
                self.add(key, value, node.left)
            else:
                node.left = Node(key, value)
        else:
            if node.right is not None:
                self.add(key, value, node.right)
            else:
                node.right = Node(key, value)

    def search(self, key):
        """
        Search value in tree
        Arguments
        --------
        key, key of a node

        Return
        --------
        Node: if find key
        None: if key not found
        """
        if (self.root is None):
            return None
        else:
            return self.find(key, self.root)

    def find(self, key, node):
        """
        Find node with key
        Arguments
        --------
        key: key to search
        node: node to search

        Return
        --------
        Node: if found
        None: not found
        """
        if key == node.key:
            return node
        elif node.right is None and node.left is None:
            return None
        elif key < node.key and node.left is not None:
            return self.find(key, node.left)
        elif key > node.key and node.right is not None:
            return self.find(key, node.right)
