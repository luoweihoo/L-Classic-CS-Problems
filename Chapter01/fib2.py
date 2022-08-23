number_of_call = 0

def fib2(n: int) -> int:
    global number_of_call
    number_of_call += 1
    if n < 2: # base case
        return n
    return fib2(n - 1) + fib2(n - 2)

if __name__ == "__main__":
    # print(fib2(-1))
    # print(fib2(0))
    # print(fib2(1))
    # print(fib2(2))
    # print(fib2(3))
    # print(fib2(4))
    # print(fib2(5))
    # print(fib2(6))
    # print(fib2(7))
    # print(fib2(8))
    # print(fib2(9))
    print(fib2(20))
    print(f'Number of call is {number_of_call}')
    