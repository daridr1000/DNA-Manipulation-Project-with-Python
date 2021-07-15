class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next = None):
        self._element = element
        self._next = next

class LinkedList:

    def __init__(self):
        self._head = None
        self._size = 0

    def add_first(self,e):
        newest = _Node(e)
        newest._next = self._head
        self._head = newest
        self._size += 1

    def add_after_node(self,previous_node,e):
        newest = _Node(e)
        if previous_node is None:
            self._head = newest
            return newest
        previous_node._next = newest
        self._size +=1
        return newest

    def print_list(self):
        val = self._head
        while val is not None:
            if val._next is None:
                print(val._element)
            else:
                print(val._element, end = "")
            val = val._next
    def get_head(self):
        return self._head
