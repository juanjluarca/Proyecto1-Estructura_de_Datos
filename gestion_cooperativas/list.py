import pickle

from node import Node
from typing import TypeVar, Generic
T = TypeVar('T')


class List(Generic[T]):
    def __init__(self):
        self.__head: Node[T] | None = None
        self.__tail: Node[T] | None = None
        self.__size = 0
        self.__current: Node[T] | None = None

    # Métodos de inserción
    def append(self, data: T):
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
            self.__size += 1
        else:
            self.__tail.next = new_node
            self.__tail = new_node
            self.__size += 1

    def prepend(self, data: T):
        new_node = Node(data, self.__head)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
            self.__size += 1
        else:
            new_node.next = self.__head
            self.__head = new_node
            self.__size += 1

    def insert_at(self, index: int, data: T):
        if index == 0:
            self.prepend(data)
            self.__size += 1
        elif index == len(self) - 1:
            self.append(data)
            self.__size += 1
        elif index < 0 or index > len(self):
            raise IndexError
        else:
            new_node = Node(data)
            previous_node = self.find_at(index - 1)
            new_node.next = previous_node.next
            previous_node.next = new_node
            self.__size += 1

    def insert_ordered(self, data: T):
        self.append(data)
        self.order_data()

    # Métodos de eliminación
    def shift(self) -> T:
        if self.is_empty():
            raise ReferenceError('No hay datos en la lista')
        elif self.__head is self.__tail:
            current = self.__head
            self.__head = None
            self.__tail = None
            self.__size = 0
            return current.data
        else:
            current = self.__head
            self.__head = current.next
            current.next = None
            self.__size -= 1

            return current.data

    def pop(self) -> T:
        if self.is_empty():
            raise ReferenceError('No hay datos en la lista')
        elif self.__head is self.__tail:
            current = self.__head
            self.__head = None
            self.__tail = None
            self.__size = 0
            return current.data
        else:
            current = self.__tail
            previous = self.find_at(len(self) - 2)
            self.__tail = previous
            previous.next = None
            self.__size -= 1

            return current.data

    def remove_at(self, index: int) -> T:
        if index < 0 or index >= len(self):
            raise IndexError('La posición no existe')
        elif index == 0:
            return self.shift()
        elif index == len(self) - 1:
            return self.pop()
        else:
            current_node = self.find_at(index)
            previous_node = self.find_at(index - 1)
            next_node = current_node.next

            previous_node.next = next_node
            current_node.next = None
            self.__size -= 1

            return current_node.data

    # Métodos de búsqueda
    def find_at(self, index: int,) -> Node[T]:
        current_index = 0
        current = self.__head

        while True:
            if current is None:
                break
            elif current_index == index:
                return current
            else:
                current = current.next
                current_index += 1
        raise IndexError('La posición no existe')

    # Métodos auxiliares
    def change_head_tail(self):
        current = self.__head
        current2 = self.__tail
        previous = self.find_at(len(self) - 2)
        if self.is_empty():
            pass
        elif len(self) == 1:
            pass
        else:
            current2.next = self.__head.next
            self.__head = current2
            self.__tail = current
            self.__tail.next = None
            previous.next = self.__tail

    def order_data(self):
        container = list()
        for data in self:
            container.append(data)
        container.sort()
        for _ in self:
            self.shift()
        for data in container:
            self.append(data)

    def order_data2(self):
        current = self.__head
        current_index = 0
        while current is not None:
            next_node = current.next
            while next_node is not None:
                if current.data > next_node.data:
                    current = current.next
                    current_index += 1
                else:
                    current = current.next

    def is_empty(self):
        return self.__head is None and self.__tail is None

    @staticmethod
    def save_data(data):
        with open('Save_editor_text.dat', 'wb') as file:
            pickle.dump(data, file)

    def __iter__(self):
        self.__current = self.__head
        return self

    def __next__(self):
        if self.__current is None:
            raise StopIteration
        data = self.__current.data
        self.__current = self.__current.next

        return data

    def __len__(self):
        cont = 0
        for _ in self:
            cont += 1
        return cont
