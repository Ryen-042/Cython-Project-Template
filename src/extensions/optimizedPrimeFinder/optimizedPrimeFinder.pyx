# cython: language_level = 3str

"""This module contains the cython versions of the prime number finder."""


from numpy cimport ndarray, int32_t
import numpy as np


cpdef inline ndarray[int32_t, ndim=1] optimized_prime_finder(int start=2, int end=100_000):
    """Find prime numbers in the range `[start:end]`. Limits are `[1:100_000]`."""
    
    if start >= end:
        raise ValueError("Start must be less than end.")
    
    if start <= 1:
        start = 2
    
    if end > 100_000:
        end = 100_000
    
    # The count of all the primes in 100_000 is 9592.
    cdef ndarray[int32_t, ndim=1] primes = np.zeros(9592, dtype=np.int32)
    
    # Creating a memoryview of the primes array.
    cdef int[:] primes_view = primes
    
    cdef int i, counter
    counter = 0
    
    for i in range(start, end + 1):
        if is_prime(i):
            primes_view[counter] = i
            counter += 1
    
    return primes[:counter]

cdef inline bint is_prime(int num) noexcept:
    """"Return True if num is prime."""
    
    cdef int i
    
    # Iterate from 2 to n / 2
    for i in range(2, num):
        # If num is divisible by any number between 2 and n / 2, it is not prime
        if (num % i) == 0:
            return False
    
    return True
