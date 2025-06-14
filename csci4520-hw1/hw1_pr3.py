class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f'Node [{self.value}]'

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, x):
        if self.first is None:
            self.first = Node(x, None)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(x, None)
            self.first.next = self.last
        else:
            current = Node(x, None)
            self.last.next = current
            self.last = current

    def __str__(self):
        if self.first is None:
            return 'LinkedList []'
        current = self.first
        out = f'LinkedList [{current.value}'
        while current.next is not None:
            current = current.next
            out += f" {current.value}"
        return f'{out}]'

    def clear(self):
        self.__init__()

    def first_index_of(self, x):
        current = self.first
        index = 0
        while current:
            if current.value == x:
                return index
            current = current.next
            index += 1
        return None

    def get_middle(self):
        slow = self.first
        fast = self.first
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        if fast:
            return [slow.value]
        else:
            return [prev.value, slow.value] if prev else []

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    for val in [1, 2, 3, 4, 5, 6]:
        ll.insert(val)
    print("Linked list:", ll)
    print("First index of 4:", ll.first_index_of(4))
    print("Middle node(s):", ll.get_middle())
