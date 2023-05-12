def collatz_step(n):
    """Compute one step in Collatz conjecture"""
    return n // 2 if n % 2 == 0 else n * 3 + 1


if __name__ == '__main__':
    print(collatz_step(4))
    print(collatz_step(5))
