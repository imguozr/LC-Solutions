from collections import OrderedDict


class LRUCache1:
    """
        Use OrderedDict.
        If the data was reused(get), should move it to the end of the dict.
    """

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(False)


class LRUCache2:
    """
        Use dict and 2 double linked list to implement.
    """

    class DoubleListNode:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.head = self.DoubleListNode()
        self.tail = self.DoubleListNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = self.DoubleListNode(key, value)
            self.cache[key] = node
            self._add_node(node)

            if len(self.cache) > self.cap:
                tail = self._pop_tail()
                self.cache.pop(tail.key)
        else:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)

    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        pre = node.prev
        nxt = node.next

        pre.next = nxt
        nxt.prev = pre

    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
