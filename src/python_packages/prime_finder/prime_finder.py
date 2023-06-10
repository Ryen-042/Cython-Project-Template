"""This module contains the python version of the prime number finder."""

from prime_finder_configs import MAX_ALLOWED_NUM, MIN_ALLOWED_NUM

def find_primes(start=2, end=100_000) -> list[int]:
    """Find prime numbers in the range `[start:end]`."""
    
    if start >= end:
        raise ValueError("Start must be less than end.")
    
    if start < MIN_ALLOWED_NUM:
        print(f"Warning: the parameter 'start' has been set to (2) instead of the provided value ({start}) as it is less than the allowed value.")
        
        start = MIN_ALLOWED_NUM
    
    if end > MAX_ALLOWED_NUM:
        print(f"Warning: the parameter 'end' has been set to ({MAX_ALLOWED_NUM}) instead of the provided value ({end}) as it exceeds the allowed limit.")
        
        end = MAX_ALLOWED_NUM
    
    primes: list[int] = []
    
    for i in range(start, end + 1):
        if is_prime(i):
            primes.append(i)
    
    return primes


def is_prime(num: int) -> bool:
    """Return True if num is prime."""
    
    # Handle even numbers separately
    if num == 2:
        return True
    
    elif num % 2 == 0 or num == 1:
        return False
    
    # Iterate from 3 to the square root of num
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    
    return True
