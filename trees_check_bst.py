'''
For the purposes of this challenge, we define a binary search tree to be a binary tree with the following ordering properties:

The  value of every node in a node's left subtree is less than the data value of that node.
The  value of every node in a node's right subtree is greater than the data value of that node.
Given the root node of a binary tree, can you determine if it's also a binary search tree?

Complete the function in your editor below, which has  parameter: a pointer to the root of a binary tree. It must return a boolean denoting whether or not the binary tree is a binary search tree. You may have to write one or more helper functions to complete this challenge.

Note: A binary tree is not a binary search if there are duplicate values.

Input Format

You are not responsible for reading any input from stdin. Hidden code stubs will assemble a binary tree and pass its root node to your function as an argument.

Constraints

Output Format

You are not responsible for printing any output to stdout. Your function must return true if the tree is a binary search tree; otherwise, it must return false. Hidden code stubs will print this result as a Yes or No answer on a new line.

Sample Input

tree

Sample Output

No
Explanation

The tree in the diagram does not satisfy the ordering property for a Binary Search Tree, so we print No.
'''

import sys

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def check_node(root, min, max):
    if root.data < min or root.data > max:
        return False
    elif root.right == None and root.left == None:
        return True
    elif root.right == None and root.left != None:
        return check_node(root.left, min, root.data - 1)
    elif root.left == None and root.right != None:
        return check_node(root.right, root.data + 1, max)
    else:
        return check_node(root.left, min, root.data - 1) and check_node(root.right, root.data + 1, max)


def check_binary_search_tree_(root):
    return check_node(root, -1, sys.maxint)