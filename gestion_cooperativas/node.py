from __future__ import annotations
from typing import TypeVar, Generic
T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, data: T, next_node=None, prev_node=None):
        self.__data = data
        self.__next: Node | None = next_node
        self.__prev: Node | None = prev_node

    @property
    def data(self):
        return self.__data

    @property
    def next(self):
        return self.__next

    @property
    def prev(self):
        return self.__prev

    @next.setter
    def next(self, new_next: Node[T]):
        self.__next = new_next

    @prev.setter
    def prev(self, new_prev: Node[T]):
        self.__prev = new_prev

    def __str__(self):
        return str(self.__data)
