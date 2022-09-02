from functools import lru_cache

number_of_call = 0

@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    global number_of_call
    number_of_call += 1
    if n < 2: # base case
        return n
    return fib4(n - 1) + fib4(n - 2)

if __name__ == "__main__":
    print(fib4(50))
    print(f'Number of call is {number_of_call}')
    