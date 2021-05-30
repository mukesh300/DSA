class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DLinkedList:
    def __init__(self, data=None):
        self.head = None
        if data:
            self.create_from_itr(data)

    def __len__(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def __add__(self, other):
        itr = self.head
        new_node = Node(other)
        if itr is None:
            self.head = new_node
            return
        while itr.next:
            itr = itr.next
        itr.next = new_node
        new_node.prev = itr

    def __str__(self):
        itr = self.head
        elements = ""
        while itr:
            elements += f"{itr.data}-->"
            itr = itr.next
        return elements[:-3]

    def create_from_itr(self, data):
        try:
            iter(data)
        except TypeError as te:
            print(data, 'is not iterable')
        if len(data) != 0:
            self.head = Node(data[0])
            if len(data) > 0:
                for val in data[1:]:
                    self + val

    def reverse(self):
        itr = self.head
        while itr:
            itr.next, itr.prev = itr.prev, itr.next
            prev = itr
            itr = itr.prev
        self.head = prev

    def insert(self, index, val):
        if 0 > index > len(self):
            raise Exception("Invalid Index")
        new_node = Node(val)
        itr = self.head
        if index == 0:
            self.head = new_node
            new_node.next = itr
            itr.prev = new_node
            return
        while index > 0:
            prev = itr
            itr = itr.next
            index -= 1
        itr = prev
        if itr.next:
            prev = itr.prev
            prev.next = new_node
            new_node.prev = prev
            new_node.next = itr
            itr.prev = new_node
            return
        itr.next = new_node
        new_node.prev = itr

    def remove(self, val):
        itr = self.head
        if itr.data == val:
            self.head = itr.next
            itr.next.prev = None
            return
        while itr.next:
            if itr.data == val:
                prev = itr.prev
                next = itr.next
                prev.next = next
                next.prev = prev
                return
            itr = itr.next
        itr.prev.next = None


if __name__ == "__main__":
    D = DLinkedList([1, 2, 3, 4, 5])
    D.insert(5, 10)
    D.reverse()
    D.remove(1)
    print(D)
