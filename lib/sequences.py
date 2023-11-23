#!/usr/bin/env python3

def print_fibonacci(length):
    fib_sequence = []  
    while len(fib_sequence) < length:
        if len(fib_sequence) < 2:
            fib_sequence.append(len(fib_sequence))
        else:
            next_number = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_number)

    print(fib_sequence)
print_fibonacci(9)

pass