"""
Prime Number Utilities

This module provides functions for working with prime numbers.
"""


def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n: Integer to check
        
    Returns:
        bool: True if n is prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def generate_primes(limit):
    """
    Generate all prime numbers up to a given limit using the Sieve of Eratosthenes.
    
    Args:
        limit: Upper bound (inclusive) for prime generation
        
    Returns:
        list: List of prime numbers up to limit
    """
    if limit < 2:
        return []
    
    # Create a boolean array and initialize all entries as true
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    
    p = 2
    while p * p <= limit:
        if sieve[p]:
            # Mark all multiples of p as not prime
            for i in range(p * p, limit + 1, p):
                sieve[i] = False
        p += 1
    
    # Collect all numbers that are still marked as prime
    return [i for i in range(limit + 1) if sieve[i]]


def nth_prime(n):
    """
    Find the nth prime number (1-indexed).
    
    Args:
        n: Which prime number to find (1st, 2nd, 3rd, etc.)
        
    Returns:
        int: The nth prime number
    """
    if n < 1:
        raise ValueError("n must be a positive integer")
    
    count = 0
    num = 2
    
    while True:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1


def prime_factors(n):
    """
    Find all prime factors of a number.
    
    Args:
        n: Integer to factorize
        
    Returns:
        list: List of prime factors
    """
    if n < 2:
        return []
    
    factors = []
    
    # Handle factor of 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Handle odd factors
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    
    # If n is still greater than 1, it's a prime factor
    if n > 1:
        factors.append(n)
    
    return factors


if __name__ == "__main__":
    # Demonstration of the functions
    print("Prime Number Utilities Demo")
    print("=" * 40)
    
    # Check if numbers are prime
    test_numbers = [2, 3, 4, 17, 20, 29, 100]
    print("\nChecking if numbers are prime:")
    for num in test_numbers:
        print(f"{num}: {is_prime(num)}")
    
    # Generate primes up to 50
    print("\nPrimes up to 50:")
    primes = generate_primes(50)
    print(primes)
    
    # Find first 10 prime numbers
    print("\nFirst 10 prime numbers:")
    first_10_primes = [nth_prime(i) for i in range(1, 11)]
    print(first_10_primes)
    
    # Find prime factors
    print("\nPrime factors:")
    test_factors = [12, 30, 100, 17]
    for num in test_factors:
        print(f"{num}: {prime_factors(num)}")
