from random import randint


def _decompose(n):
    i = 0
    while n & (1 << i) == 0:
        i += 1
    return i, n >> i


def _is_prime(n):
    if n % 2 == 0:
        return False

    for i in range(1, 40):
        a = randint(1, n - 1)
        if _is_composite(a, n):
            return False
    return True


def _is_composite(a, n):
    
    t,d = _decompose(n - 1)
    x = pow(a, d, n)
    
    if x == 1 or x == n - 1:
        return False

    for i in range(1, t):
        x0 = x;
        x = pow(x0, 2, n)
        if x == 1 and x0 != 1 and x0 != n - 1:
            return True
    if x != 1:
        return True
        
    return False


def _extended_euclid(a, b):
    if b == 0:
        return a, 1, 0
    else: 
        d2, x2, y2 = _extended_euclid(b, a % b)
        d, x, y = d2, y2, x2 - (a // b) * y2
        return d, x, y


def get_random_prime(prime_size):
    x = randint(1 << (prime_size - 1), (1 << prime_size) - 1)
    while not (_is_prime(x)):
        x = randint(1 << (prime_size - 1), (1 << prime_size) - 1) 
    return x
    

def multiplicative_inverse(e, phi):
        return _extended_euclid(e, phi)[1] % phi
