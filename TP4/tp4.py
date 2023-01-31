# encoding utf-8
"""This program is used to create a binary tree
we can add a node, display the tree in deep or wide path"""
class BinaryTree():
    """This class is used to create a root to the binary tree"""
    def __init__(self):
        self.root=None

    def print_tree(self):
        """display the tree from the root"""
        return f"The wide path of the tree :\n{self.root.display_node()}\n\n"\
    f"The deep path of the tree :\n\n{self.root.display_tree_deep()}"

class Node():
    """This class is used to add a node to the binary tree
    and to display the tree"""
    def __init__(self, value):
        """This method is used to initiate a node
        it takes only value like argument"""
        self.value=value
        self.right= None
        self.left= None
        self.depth= 0

    def add(self, left = None, right = None):
        """This method is used to add a node to the left
        or the rigth side of the tree"""
        self.left = left
        self.right = right
        if self.left:
            left.depth = self.depth + 1
            left.update_children_depth()
        if self.right:
            right.depth = self.depth + 1
            right.update_children_depth()

    def update_children_depth(self):
        """This method is used to update the depth
        for each new node of the tree"""
        if self.left:
            self.left.depth = self.depth + 1
            self.left.update_children_depth()
        if self.right:
            self.right.depth = self.depth + 1
            self.right.update_children_depth()

    def display_node(self):
        """This method is used to display
        the tree on its wide path"""
        line = ""
        for _ in range(1, self.depth+1):
            line+= "\t"
        retour = f"{line}{self}"
        if self.right:
            retour += f"\n{self.right.display_node()}"
        if self.left:
            retour += f"\n{self.left.display_node()}"
        return retour
    
    def display_tree_deep(self):
        """This method is used to display
        the tree on its deep path"""
        retour = ""
        if self.left and self.right:
            if self.depth == 0:
                retour= f"\t{self}"
            retour+= "\n"
            retour+= (self.depth-1)*"\t"+ f"{self.left}"\
                f"{self.left.display_tree_deep()}\t\t{self.right}"\
                f"{self.right.display_tree_deep()}\n"
        else:
            if self.left and self.right is None:
                if self.depth == 0:
                    retour= f"\t{self}"
                retour+= "\n"
                retour+= ((self.left.depth))*"\t"+f"{self.left}{self.left.display_tree_deep()}\n"
            if self.right and self.left is None:
                if self.depth == 0:
                    retour= f"\t{self}"
                retour+= "\n"
                retour+= f"{(self.right.depth)-1}*\t"\
                    f"{self.right}{self.right.display_tree_deep()}\n"
        return retour

    def __str__(self):
        """This method is used to return
        the nodes value and depth"""
        return str(self.value) + "/" + str(self.depth)

    def is_leaf(self):
        """This method is used to check 
        if the node is a leaf or not"""
        #return self.left == None and self.right == None
        return not(self.left or self.right)

    def get_max_depth(self,max_depth=0):
        """This method is used to get
        the max depth of the tree"""
        if self.is_leaf():
            if self.depth > max_depth:
                return self.depth
            else:
                return max_depth
        else:
            if self.right:
                max_depth = self.right.get_max_depth(max_depth)
            if self.left:
                max_depth = self.left.get_max_depth(max_depth)
            return max_depth


node1 = Node(0)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node3.add(node4)
node1.add(node2, node3)
tree1=BinaryTree()
tree1.root=node1

node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node5.add(node6, node7)
node4.add(node5)
node8 = Node(8)
node7.add(node8)

print(str(node1.get_max_depth(0)))
print(node1.display_node())
print(tree1.print_tree())
print(node1.display_tree_deep())
