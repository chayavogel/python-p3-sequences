#!/usr/bin/env python3

def print_fibonacci(length):

    if length == 0:
        sequence = []
    elif length == 1:
        sequence = [0]
    elif length == 2:
        sequence = [0,1]
    else:
        sequence = [0,1,1]
        i = 4
        while i <= length:
            sequence.append(sequence[-1] + sequence[-2])
            i+=1

    print(sequence)
    return sequence
