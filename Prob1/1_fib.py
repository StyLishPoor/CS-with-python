from typing import Dict,Generator
from functools import lru_cache

memo: Dict[int,int] = {0: 0,1: 1} #基底

#lru_casheによる高速化
@lru_cache(maxsize = 5)
def fib(n:int) -> int:
    """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    """
    """
    # 辞書による高速化
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
    """

    if n == 1: return 0
    last: int = 0
    next: int = 1
    for _ in range(1,n):
        last,next = next, last+next
    return next

def fib_gen(n:int) -> Generator[int,None,None]:
    yield 0
    if n > 0: yield 1
    last: int = 0
    next: int = 1
    for _ in range(i,n):
        last,next = next,last+next
        yield  next 

if __name__ == "__main__":
    for i in fib_gen(3):
        print(i)