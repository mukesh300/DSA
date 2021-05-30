from queuex import Queue


class BinarySearchTree:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, value):
        if self.data is None:
            self.data = value
            return
        if value < self.data:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        elif value > self.data:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    def search(self, data):
        if self.data == data:
            return True
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def max(self):
        if self.right is None:
            return self.data
        return self.right.max()

    def min(self):
        if self.left is None:
            return self.data
        return self.left.min()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)

        else:
            if self.right is None and self.left is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self

    def traverse_breadth(self):
        if self.data is None: return
        itr = self
        queue = Queue()
        lst = []
        queue.enque(itr)
        while not queue.is_empty():
            itr = queue.peek()
            if itr.left:
                queue.enque(itr.left)
            if itr.right:
                queue.enque(itr.right)
            lst.append(queue.deque().data)
        return lst

    def preorder(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.preorder()
        if self.right:
            elements += self.right.preorder()
        return elements

    def inorder(self):
        elements = []
        if self.left:
            elements += self.left.inorder()
        elements.append(self.data)
        if self.right:
            elements += self.right.inorder()
        return elements

    def postorder(self):
        elements = []
        if self.left:
            elements += self.left.postorder()
        if self.right:
            elements += self.right.postorder()
        elements.append(self.data)
        return elements


if __name__ == "__main__":
    bst = BinarySearchTree()
    l = [4, 5, 3, 8, 4, 7, 1, 8]
    for val in l:
        bst.insert(val)
    bst.delete(4)
    print(bst.traverse_breadth())
    print(bst.preorder())
    print(bst.inorder())
    print(bst.postorder())
    print(bst.search(73))
    print(bst.max(), bst.min())
