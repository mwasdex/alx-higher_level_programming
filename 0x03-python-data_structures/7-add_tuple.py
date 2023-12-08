#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    A = tuple_a + (0, 0)
    B = tuple_b + (0, 0)
    new = A[0] + B[0], A[1] + B[1]
    return new
