"""Cython implementation of the is_prime function."""

class IsPrimeNamespace:
	"""This class only provides a way for other modules to import the cdef methods in this module"""

	@staticmethod
	def isPrime(num: int) -> bool:
		"""Return `True` if num is prime and `False` otherwise."""
		...
