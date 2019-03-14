def is_prime(n):
    for divisor in range(2, int(n ** 0.5)):
        if n % divisor == 0:
            return False
    return True
