from typing import Generator

def fib6(n: int) -> Generator[int, None, None]:
    yield 0                 # Special case
    if n > 0: yield 1       # Special case
    last: int = 0           # Initially set to fib(0)
    next: int = 1           # Initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
        yield next          # Main generation step

if __name__ == "__main__":
    for i in fib6(50):
        print(i)