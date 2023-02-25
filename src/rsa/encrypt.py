import os
import base64

from src.rsa.helpers import read_key


def encrypt_text(message, public_key_filepath):

    keys = read_key(public_key_filepath)
    message_bytes = message.encode('utf-8')
    encoded_message = message_bytes.hex()

    n = int(keys['n'])
    e = int(keys['e'])
    
    print('')
    print('n:',n)
    print('e:',e)

    encoded_message = int(encoded_message,16)
    encrypted_message = pow(encoded_message, e, n)
    
    print('\n**********************************')
    print('[*] Encrypted message by RSA')
    print('**********************************\n')
    
    return encrypted_message

