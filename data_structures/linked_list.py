class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def __len__(self):
        count = 0
        itr = self.headval
        while itr:
            count += 1
            itr = itr.nextval
        return count

    def __add__(self, other):
        new_node = Node(other)
        if self.headval is None:
            self.headval = new_node
            return
        itr = self.headval
        while itr.nextval:
            itr = itr.nextval
        itr.nextval = new_node

    def __str__(self):
        itr = self.headval
        elements = ''
        while itr:
            elements += f'{itr.dataval}-->'
            itr = itr.nextval
        return elements[:-3]

    def insert(self, index, other):
        if index < 0 or index >= len(self):
            raise Exception("invalid index")

        itr = self.headval
        new_val = Node(other)

        if index == 0:
            new_val.nextval = self.headval
            self.headval = new_val
            return

        index -= 1
        while index > 0:
            itr = itr.nextval
            index -= 1
        new_val.nextval = itr.nextval
        itr.nextval = new_val

    def remove(self, val):
        itr = self.headval

        if itr is not None:
            if itr.dataval == val:
                self.headval = itr.nextval
                return

        while itr:
            if itr.dataval == val:
                break
            prev = itr
            itr = itr.nextval
        prev.nextval = itr.nextval


list = SLinkedList()
week = ["mon", "tue", "thu", "fri"]
for day in week:
    list + day

list.insert(2, "sat")
list.remove("mon")
print(len(list))
print(list)
