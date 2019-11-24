import sys
from abc import ABCMeta, abstractmethod


class CustomOutBase(metaclass=ABCMeta):
    orgout = sys.stdout

    def __init__(self):
        # self.orgout = sys.stdout
        sys.stdout = self

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_value, trace):
        sys.stdout = self.orgout

    @abstractmethod
    def write(self, s: str) -> int:
        raise NotImplementedError()


def stdout_temp(newout: CustomOutBase):
    def outer(func):
        def inner(*args, **kwargs):
            with newout:
                func(*args, **kwargs)
        return inner
    return outer


def end_filter(func):
    def wrapper(*args, **kwargs):
        s = args[1]
        if isinstance(s, str):
            if s.strip() == "":
                return

            func(*args, **kwargs)
        else:
            raise TypeError()
    return wrapper


class __CustomOut(CustomOutBase):
    def write(self, s: str) -> int:
        if s.strip() == "":
            return 0

        print(f"@@@{s}@@@", file=self.orgout)
        return len(s)


if __name__ == "__main__":

    @stdout_temp(__CustomOut())
    def __printer():
        print("Hello, print!")

    def __printer2():
        print("Bye, print!")

    __printer()  # @@@Hello, print!@@@
    __printer2()  # Bye, print!
