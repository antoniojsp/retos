#!/bin/python3

import os
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def check_node(node):
    return True if node else False


def compare_lists(llist1, llist2):
    temp1, temp2 = llist1, llist2

    while temp1 and temp2:
        if temp1.data != temp2.data:
            return 0
        temp1 = temp1.next
        temp2 = temp2.next

        node1 = check_node(temp1)
        node2 = check_node(temp2)

        if node1 ^ node2:
            return 0
    return 1


if __name__ == '__main__':