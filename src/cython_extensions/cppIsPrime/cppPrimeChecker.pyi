"""Cython implementation of the is_prime function for the cpp mode."""

class IsPrimeNamespace:
	"""The only purpose of this class is to enable other cpp extensions to import the cdef methods in this module."""

	@staticmethod
	def cppIsPrime(num: int) -> bool:
		"""Return `True` if num is prime and `False` otherwise."""
		...
