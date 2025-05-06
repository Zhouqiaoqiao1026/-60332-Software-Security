# Dynamic input simulation (indeterminate)
import random

def nondet_int():
    return random.choice([0, 1, 2, 3])  # Simulate nondeterministic int

def main():
    x = nondet_int()
    y = 100 // x  # May trigger division by zero
    return y

main()