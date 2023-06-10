# distutils: language = c++
# cython: language_level = 3str

"""This module contains the c++ version of the prime number finder with vectors."""

cimport cython
from cython.parallel cimport prange, parallel
from libcpp.vector cimport vector
from prime_finder_configs import MAX_ALLOWED_NUM, MIN_ALLOWED_NUM
from cython_extensions.cppIsPrime.cppPrimeChecker cimport IsPrimeNamespace


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef vector[int] cppFindPrimes(int start=2, int end=100_000):
    """Find prime numbers in the range `[start:end]`. Utilizes 4 threads to parallelize the process."""
    
    if start >= end:
        raise ValueError("Start must be less than end.")
    
    if start < MIN_ALLOWED_NUM:
        print(f"Warning: the parameter 'start' has been set to (2) instead of the provided value ({start}) as it is less than the allowed value.")
        
        start = MIN_ALLOWED_NUM
    
    if end > MAX_ALLOWED_NUM:
        print(f"Warning: the parameter 'end' has been set to ({MAX_ALLOWED_NUM}) instead of the provided value ({end}) as it exceeds the allowed limit.")
        
        end = MAX_ALLOWED_NUM
    
    cdef vector[int] primes
    cdef vector[vector[int]] thread_primes = [vector[int]() for _ in range(4)]
    
    # Count the number of primes
    cdef int i, num, chunksize = (end - start) //4
    
    with nogil, parallel():
        for i in prange(4):
            for num in range(start + i * chunksize, start + i * chunksize + chunksize):
                if IsPrimeNamespace.cppIsPrime(num):
                    thread_primes[i].push_back(num)
    
    for i in range(4):
        primes.insert(primes.end(), thread_primes[i].begin(), thread_primes[i].end())
    
    return primes
