import time
from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def measure_time(cipher, mode, key, data):
    start_time = time.time()
    
    if cipher == 'DES':
        cipher = DES.new(key, mode)
        padded_data = pad(data, DES.block_size)
        encrypted_data = cipher.encrypt(padded_data)
        decrypted_data = cipher.decrypt(encrypted_data)
        plaintext = unpad(decrypted_data, DES.block_size)
    elif cipher == 'AES':
        cipher = AES.new(key, mode)
        padded_data = pad(data, AES.block_size)
        encrypted_data = cipher.encrypt(padded_data)
        decrypted_data = cipher.decrypt(encrypted_data)
        plaintext = unpad(decrypted_data, AES.block_size)
    
    end_time = time.time()
    
    return end_time - start_time

# Define key sizes and other parameters
message = "Performance Testing of Encryption Algorithms".encode()
des_key = get_random_bytes(8)  # DES key size is 8 bytes
aes_key = get_random_bytes(32)  # AES key size is 32 bytes for AES-256

# Measure DES performance
des_time = measure_time('DES', DES.MODE_ECB, des_key, message)

# Measure AES-256 performance
aes_time = measure_time('AES', AES.MODE_ECB, aes_key, message)

print(f"Time taken for DES (ECB mode): {des_time:.6f} seconds")
print(f"Time taken for AES-256 (ECB mode): {aes_time:.6f} seconds")
