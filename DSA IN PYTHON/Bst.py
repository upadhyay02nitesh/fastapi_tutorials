class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    def __init__(self): 
        self.root = None
    
    def is_empty(self):
        return self.root is None 
    
    def insert(self, data):
        if self.is_empty():
            self.root = Node(data)
        else:
            self.insert_recursive(self.root, data)
    
    def insert_recursive(self, root, data):
        if data < root.item:
            if root.left is None:
                root.left = Node(data)
            else:
                self.insert_recursive(root.left, data)
        else:
            if root.right is None:
                root.right = Node(data)
            else:
                self.insert_recursive(root.right, data)

    def search(self, data):
        if self.is_empty():
            return False
        else:
            if self.root.item == data:
                return True
            else:
                return self.search_recursive(self.root, data)
    
    def search_recursive(self, root, data):
        if root is None:
            return False
        
        if data == root.item:
            return True
        elif data < root.item:
            return self.search_recursive(root.left, data)
        else:
            return self.search_recursive(root.right, data)
      
          
    def inorder_traversal(self, root):
        if root is not None:
            self.inorder_traversal(root.left)
            print(root.item, end=" ")
            self.inorder_traversal(root.right)

    def print_inorder(self):
        if self.root is None:
            print("Tree is empty")
        else:
            print("Inorder Traversal:", end=" ")
            self.inorder_traversal(self.root)
    def preorder_traversal(self, root):
        if root is not None:
            print(root.item, end=" ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def print_preorder(self):
        if self.root is None:
            print("Tree is empty")
        else:
            print("Preorder Traversal:", end=" ")
            self.preorder_traversal(self.root)
    def postorder_traversal(self, root):
        if root is not None:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.item, end=" ")

    def print_postorder(self):
        if self.root is None:
            print("Tree is empty")
        else:
            print("Postorder Traversal:", end=" ")
            self.postorder_traversal(self.root)
    
    def min_value(self):
        if not self.is_empty():
            temp=self.root
            while temp.left!=None:
                temp=temp.left 
            return temp.item
    def max_value(self):
        if not self.is_empty():
            temp=self.root
            while temp.right!=None:
                temp=temp.right
            return temp.item
        
    def delete_root(self,data):
        self.root=self.rdelete(self.root,data)
    
    def rdelete(self, root, data):
        if root is None:
            return root
        
        if data < root.item:
            root.left = self.rdelete(root.left, data)
        elif data > root.item:
            root.right = self.rdelete(root.right, data)

        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.min_value_root(root.right)
            root.item = temp.item
            root.right = self.rdelete(root.right, temp.item)
        return root

    def min_value_root(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

# Example usage:
b = BST()
b.insert(10)   
b.insert(20)   
b.insert(5)   
b.insert(15)   
b.insert(25)   
b.print_inorder() 
print()
b.print_preorder() 
print()
b.print_postorder() 

# Accessing the root root
print()
if b.search(20):
    print("Found")
else:
    print("Not Found")
print()
print("Root Is ", b.root.item)
print()
print("Minimum Value  Is :", b.min_value())
print()
print("Maximum Value Is  :", b.max_value())
print()
b.delete_root(25)
print()
b.print_inorder() 



