#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    fib_sequence = [0, 1]
    if length == 1:
        print(fib_sequence[0])
    
    while len(fib_sequence) < length:
        nxt_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(nxt_fib)

    print(fib_sequence)

# Example:
print_fibonacci(9)