class ListNode:
    prev: ListNode | None = None
    next: ListNode | None = None
    value: int
    key: int

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value


class LRUCache:
    _capacity: int
    _cache: dict[int, ListNode]
    _head: ListNode | None = None
    _tail: ListNode | None = None

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = dict()

    # Detaches and move to head
    def move_to_head(self, node: ListNode) -> ListNode:
        if node is not self._head:
            predecessor = node.prev
            succcessor = node.next
            if predecessor is not None:
                predecessor.next = succcessor
            if succcessor is not None:
                succcessor.prev = predecessor
            if node is self._tail:
                self._tail = predecessor
            node.next = self._head
            node.prev = None
            self._head.prev = node
            self._head = node
            return node

    def get(self, key: int) -> int:
        if key in self._cache:
            node = self._cache[key]
            value = node.value
            node = self.move_to_head(node)
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            node = self._cache[key]
            node.value = value
            # links the detached nodes
            self.move_to_head(node)
        else:
            if len(self._cache) == self._capacity:
                deletion_node = self._tail
                self._tail = deletion_node.prev
                if self._tail is not None:
                    self._tail.next = None
                if self._head is deletion_node:
                    self._head = None
                del self._cache[deletion_node.key]
            node = ListNode(key, value)
            if self._head is None:
                self._head = node
                self._tail = node
            else:
                # should attach the new node to the head
                node = self.move_to_head(node)
            self._cache[key] = node
