cdef class IsPrimeNamespace:
    @staticmethod
    cdef bint cppIsPrime(int num) noexcept nogil