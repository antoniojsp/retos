import heapq


class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._items_map = {}

    def insert(self, item, priority):
        if item in self._items_map:
            raise ValueError(f"Item {item} already exists in the queue!")

        heapq.heappush(self._heap, (priority, item))
        self._items_map[item] = -priority

    def pop(self):
        if not self._heap:
            raise KeyError("Pop from an empty priority queue!")

        item, priority = heapq.heappop(self._heap)
        del self._items_map[item]
        return item

    def is_empty(self):
        return not self._heap

    def print(self):
        print(self._heap, self._items_map)

pq = PriorityQueue()
pq.insert('task1', 3)
pq.insert('task2', 1)
pq.insert('task3', 2)
pq.print()
print(pq.pop())  # Output: task2
# print(pq.pop())  # Output: task3
# print(pq.pop())  # Output: task1
# print(pq.is_empty())  # Output: True
# import heapq
# import time
#
#
# class PriorityQueue:
#     def __init__(self):
#         self.heap = []
#         self.counter = 0
#
#     def insert(self, item, priority):
#         entry = (priority, self.counter, item)
#         heapq.heappush(self.heap, entry)
#         self.counter += 1
#
#     def pop(self):
#         if not self.is_empty():
#             return heapq.heappop(self.heap)[2]
#         else:
#             return None
#
#     def is_empty(self):
#         return len(self.heap) == 0
#
#
# # Usage example
# pq = PriorityQueue()
# pq.insert('task1', 3)
# pq.insert('task2', 1)
# pq.insert('task3', 2)
#
# print(pq.pop())  # Output: task2
# print(pq.pop())  # Output: task3
# print(pq.pop())  # Output: task1
# print(pq.is_empty())  # Output: True
