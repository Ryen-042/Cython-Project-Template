# cython: language_level = 3str

"""This module contains an optimized implementation of the prime number finder."""

cimport cython
from cython.parallel import prange, parallel
cimport numpy as np
import numpy as np
from prime_finder_configs import MAX_ALLOWED_NUM, MIN_ALLOWED_NUM
from cython_extensions.isPrime.primeChecker cimport IsPrimeNamespace


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef np.ndarray[np.int32_t, ndim=1] optimizedFindPrimes(int start=2, int end=100_000):
    """A fast implementation for finding prime numbers in the range `[start:end]`. It utilizes 4 threads to parallelize the process."""
    
    if start >= end:
        raise ValueError("Start must be less than end.")
    
    if start < MIN_ALLOWED_NUM:
        print(f"Warning: the parameter 'start' has been set to (2) instead of the provided value ({start}) as it is less than the allowed value.")
        start = MIN_ALLOWED_NUM
    
    if end > MAX_ALLOWED_NUM:
        print(f"Warning: the parameter 'end' has been set to ({MAX_ALLOWED_NUM}) instead of the provided value ({end}) as it exceeds the allowed limit.")
        end = MAX_ALLOWED_NUM
    
    cdef int i, num, counter, chunksize = (end - start) // 4
    cdef int * counter_ptr
    
    # Allocate memory for thread-specific primes arrays
    cdef np.ndarray[np.int32_t, ndim=2] thread_primes = np.zeros((4, chunksize), dtype=np.int32)
    
    # Thread-specific counts of primes.
    cdef int[4] counts
    
    cdef int[:, :] primes_view = thread_primes
    
    with nogil, parallel():
        for i in prange(4):
            counter = 0
            counter_ptr = &counter
            for num in range(start + i * chunksize, start + i * chunksize + chunksize):
                if IsPrimeNamespace.isPrime(num):
                    primes_view[i][counter] = num
                    counter_ptr[0] += 1
            
            # Update the count of primes for the current thread
            counts[i] = counter
    
    # Combine the primes from all threads.
    return np.concatenate([primes[:counts[i]] for i, primes in enumerate(thread_primes)])