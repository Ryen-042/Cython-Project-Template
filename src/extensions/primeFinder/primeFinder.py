"""This module contains the python versions of the prime number finder."""

def prime_finder(start=2, end=100_000) -> list[int]:
    """Find prime numbers in the range `[start:end]`. Limits are `[1:100_000]`."""
    
    if start >= end:
        raise ValueError("Start must be less than end.")
    
    if start <= 1:
        start = 2
    
    if end > 100_000:
        end = 100_000
    
    primes: list[int] = []
    
    for i in range(start, end + 1):
        if is_prime(i):
            primes.append(i)
    
    return primes

def is_prime(num: int) -> bool:
    """"Return True if num is prime."""
    
    # Iterate from 2 to n / 2
    for i in range(2, num):
        # If num is divisible by any number between 2 and n / 2, it is not prime
        if (num % i) == 0:
            return False
    
    return True
