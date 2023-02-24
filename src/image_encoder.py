import cv2 
import numpy as np   
from src.utils.to_bin import to_bin 
from src.rsa.generate_keys import generate_keys
from src.rsa.encrypt import encrypt_text

def encode(image_name, secret_data, public_key, n_bits=2):

    # encrypt the secret data 
    secret_data = str(encrypt_text(secret_data, public_key))
    # read the image
    image = cv2.imread(image_name)
    # maximum bytes to encode
    n_bytes = image.shape[0] * image.shape[1] * 3 * n_bits // 8
    print("[*] Maximum bytes to encode:", n_bytes)
    print("[*] Data size:", len(secret_data))
    if len(secret_data) > n_bytes:
        raise ValueError(f"[!] Insufficient bytes ({len(secret_data)}), need bigger image or less data.")
    print("[*] Encoding data...")
    # add stopping criteria
    if isinstance(secret_data, str):
        secret_data += "====="
    elif isinstance(secret_data, bytes):
        secret_data += b"====="
    data_index = 0
    # convert data to binary
    binary_secret_data = to_bin(secret_data)
    # size of data to hide
    data_len = len(binary_secret_data)
    for bit in range(1, n_bits+1):
        for row in image:
            for pixel in row:
                # convert RGB values to binary format
                r, g, b = to_bin(pixel)
                # modify the least significant bit only if there is still data to store
                if data_index < data_len:
                    if bit == 1:
                        # least significant red pixel bit    
                        pixel[0] = int(r[:-bit] + binary_secret_data[data_index], 2)
                    elif bit > 1:
                        # replace the `bit` least significant bit of the red pixel with the data bit
                        pixel[0] = int(r[:-bit] + binary_secret_data[data_index] + r[-bit+1:], 2)
                    data_index += 1
                if data_index < data_len:
                    if bit == 1:
                        # least significant green pixel bit
                        pixel[1] = int(g[:-bit] + binary_secret_data[data_index], 2)
                    elif bit > 1:
                        # replace the `bit` least significant bit of the green pixel with the data bit
                        pixel[1] = int(g[:-bit] + binary_secret_data[data_index] + g[-bit+1:], 2)
                    data_index += 1
                if data_index < data_len:
                    if bit == 1:
                        # least significant blue pixel bit
                        pixel[2] = int(b[:-bit] + binary_secret_data[data_index], 2)
                    elif bit > 1:
                        # replace the `bit` least significant bit of the blue pixel with the data bit
                        pixel[2] = int(b[:-bit] + binary_secret_data[data_index] + b[-bit+1:], 2)
                    data_index += 1
                # if data is encoded, just break out of the loop
                if data_index >= data_len:
                    break
    return image