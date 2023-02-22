import os
import sys

from math import gcd

from rsa.utils.math import get_random_prime, multiplicative_inverse


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
    filepath = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
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
    #p = get_random_prime(prime_size)
    p = 8621272829000603383141872679731572853887466295796883868134183836024988031107749781762709757340651359468466847965567109140301447779667281775513509492789527
    #q = get_random_prime(prime_size)
    q = 10472087380680040720306459817487077878715570507742806645619782301655711347445552392656057595334459639236638207892018342088664046537110766437018693826942803

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
    print("p: ", p)
    print("q: ", q)
    _write_key(public_key)
    _write_key(private_key,'private')


if __name__ == "__main__":
    generate_keys()