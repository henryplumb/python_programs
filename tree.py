#!/usr/env/python

class BinaryNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addItem(self, item):
        if self.data == item:
            print("Item already exists!")
            return False
        else:
            if item < self.data:
                if self.left is not None:
                    self.left.addItem(item)
                else:
                    self.left = BinaryNode(item)
                    print("Created node left of '" + self.data + "' : '" + item + "'")
            else:
                if self.right is not None:
                    self.right.addItem(item)
                else:
                    self.right = BinaryNode(item)
                    print("Created node right of '" + self.data + "' : '" + item + "'")

    def inOrder(self, node):
        if node.left is not None: self.inOrder(node.left)
        print(node.data)
        if node.right is not None: self.inOrder(node.right)

    def preOrder(self, node):
        print(node.data)
        if node.left is not None: self.preOrder(node.left)
        if node.right is not None: self.preOrder(node.right)

    def postOrder(self, node):
        if node.left is not None: self.postOrder(node.left)
        if node.right is not None: self.postOrder(node.right)
        print(node.data)

    def reverseOrder(self, node):
        if node.right is not None: self.reverseOrder(node.right)
        print(node.data)
        if node.left is not None: self.reverseOrder(node.left)

root = None

while True:
    cmd = input("Add, remove or list data? ")
    if cmd == "add":
        data = None
        while data is not "":
            data = input("Data to add: ")
            if data is not "":
                if root is None:
                    root = BinaryNode(data)
                    print("Created root node: " + data)
                else:
                    root.addItem(data)
    elif cmd == "in-order":
        root.inOrder(root)
    elif cmd == "pre-order":
        root.preOrder(root)
    elif cmd == "post-order":
        root.postOrder(root)
    elif cmd == "reverse-order":
        root.reverseOrder(root)
