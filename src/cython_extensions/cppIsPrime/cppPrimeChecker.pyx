# distutils: language = c++
# cython: language_level = 3str

"""Cython implementation of the is_prime function for the cpp mode."""

cimport cython

cdef extern from "math.h":
    double sqrt(int x) nogil

cdef class IsPrimeNamespace:
    """The only purpose of this class is to enable other cpp extensions to import the cdef methods in this module."""
    
    @cython.boundscheck(False)
    @cython.wraparound(False)
    @cython.cdivision(True)
    @staticmethod
    cdef public inline bint cppIsPrime(int num) noexcept nogil:
        """Return `True` if num is prime and `False` otherwise."""
        
        # Handle even numbers separately
        if num == 2:
            return True
        
        elif num % 2 == 0 or num == 1:
            return False
        
        cdef int i, limit
        limit = int(sqrt(num) + 1)
        
        # Iterate from 3 to the square root of num
        for i in range(3, limit, 2):
            if num % i == 0:
                return False
        
        return True
