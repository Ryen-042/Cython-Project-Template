# cython: language_level = 3str

"""This module contains a basic implementation of the prime number finder."""

cimport cython
import numpy as np
cimport numpy as np
from cython_extensions.isPrime.primeChecker cimport IsPrimeNamespace
from prime_finder_configs import MAX_ALLOWED_NUM, MIN_ALLOWED_NUM


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef np.ndarray[np.int32_t, ndim=1] findPrimes(int start=2, int end=100_000):
    """A simple implementation for finding prime numbers in the range `[start:end]`."""
    
    if start >= end:
        raise ValueError("Start must be less than end.")
    
    if start < MIN_ALLOWED_NUM:
        print(f"Warning: the parameter 'start' has been set to (2) instead of the provided value ({start}) as it is less than the allowed value.")
        start = MIN_ALLOWED_NUM
    
    if end > MAX_ALLOWED_NUM:
        print(f"Warning: the parameter 'end' has been set to ({MAX_ALLOWED_NUM}) instead of the provided value ({end}) as it exceeds the allowed limit.")
        end = MAX_ALLOWED_NUM
    
    cdef np.ndarray[np.int32_t, ndim=1] primes = np.zeros(int((end - start)//2 + 1), dtype=np.int32)
    
    # Creating a memoryview of the primes array.
    cdef int[:] primes_view = primes
    
    cdef int i, counter
    counter = 0
    for i in range(start, end + 1):
        if IsPrimeNamespace.isPrime(i):
            primes_view[counter] = i
            counter += 1
    
    return primes[:counter]