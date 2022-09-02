from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1}     # our base cases
number_of_call = 0

def fib3(n: int) -> int:
    global number_of_call
    number_of_call += 1
    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n-2) # memoization
    return memo[n]

if __name__ == "__main__":
    print(fib3(20)) 
    print(f'Number of call is {number_of_call}')


