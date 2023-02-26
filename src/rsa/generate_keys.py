import os
import sys

from math import gcd

from src.utils.math import get_random_prime, multiplicative_inverse


def get_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    for i in range(2, phi):
        if gcd(phi,i) == 1:
            e = i
            break
         
    d = multiplicative_inverse(e, phi)
    
    return n, e, d

def _write_key(keydict, filetype='public'):
    filename = '{}.key'.format(filetype)

    if filetype == 'private':
        filepath = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            filename
        )
    else:
        # Public key is saved outside of the src directory
        filepath = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))),
            filename
        )


    f = open(filepath, "w")
    for key in keydict:
        f.write('{key}:{value}\n'.format(
            key=key,
            value=keydict[key]
        ))
    f.close()

    print('Successfully generated key: {}'.format(filename))
    print('{} path: {}'.format(
        filename,
        filepath
    ))
    print('')


def generate_keys():
    modulus_size = 1024
    prime_size = modulus_size // 2

    # Generate primes
    p = get_random_prime(prime_size)
    q = get_random_prime(prime_size)

    while p == q:
        q = get_random_prime(prime_size)

    n, e, d = get_keys(p, q)

    public_key = {
        'n': n,
        'e': e
    }

    private_key = {
        'n': n,
        'd': d
    }
    _write_key(public_key)
    _write_key(private_key,'private')


if __name__ == "__main__":
    generate_keys()