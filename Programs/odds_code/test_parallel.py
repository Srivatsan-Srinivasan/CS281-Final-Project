import concurrent.futures
from time import time


l = list(range(int(1e8)))


def f(n):
    return n+1


def main():
    t0 = time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for e, res in zip(l, executor.map(f, l)):
            res += 1
    print(time() - t0)
