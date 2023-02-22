import cv2  
import argparse
import os
from image_decoder import decode 
from image_encoder import encode  


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Steganography encoder/decoder, this Python scripts encode data within images.")
    parser.add_argument("-t", "--text", help="The text data to encode into the image, this only should be specified for encoding", default="Luong Son Thang")
    parser.add_argument("-f", "--file", help="The file to hide into the image, this only should be specified while encoding")
    parser.add_argument("-e", "--encode", help="Encode the following image", default="images/input_images/bk.png")
    parser.add_argument("-d", "--decode", help="Decode the following image", default="images/output_images/bk_encoded.png")
    parser.add_argument("-b", "--n-bits", help="The number of least significant bits of the image to encode", type=int, default=2)
    # parse the args
    args = parser.parse_args()
    if args.encode != "0":
        # if the encode argument is specified
        if args.text:
            secret_data = args.text
        elif args.file:
            with open(args.file, "rb") as f:
                secret_data = f.read()
        input_image = args.encode
        # split the absolute path and the file
        _, file = os.path.split(input_image)
        # split the filename and the image extension
        filename, ext = file.split(".")
        output_image = os.path.join("./images/output_images/", f"{filename}_encoded.{ext}")
        # encode the data into the image
        encoded_image = encode(image_name=input_image, secret_data=secret_data, n_bits=args.n_bits)
        # save the output image (encoded image)
        cv2.imwrite(output_image, encoded_image)
        print("[+] Saved encoded image.")
    if args.decode != "0":
        input_image = args.decode
        if args.file:
            # decode the secret data from the image and write it to file
            decoded_data = decode(input_image, n_bits=args.n_bits, in_bytes=True)
            with open(args.file, "wb") as f:
                f.write(decoded_data)
            print(f"[+] File decoded, {args.file} is saved successfully.")
        else:
            # decode the secret data from the image and print it in the console
            decoded_data = decode(input_image, n_bits=args.n_bits)
            print("[+] Decoded data:", decoded_data)