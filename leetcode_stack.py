class CustomStack:
    def __init__(self, maxSize: int):
        self.__stack = []
        self.__maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.__stack) < self.__maxSize:
            self.__stack.append(x)

    def pop(self) -> int:
        if self.__stack:
            return self.__stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        if k > len(self.__stack):
            k = len(self.__stack)
        for i in range(k):
            self.__stack[i] += val

    @property
    def stack(self):
        return self.__stack
