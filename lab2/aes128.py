from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt_message(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)  # Using ECB mode
    padded_text = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext

def decrypt_message(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)  # Using ECB mode
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext, AES.block_size).decode()
    return plaintext

# Key should be 16 bytes for AES-128
key = bytes.fromhex("0123456789ABCDEF0123456789ABCDEF")

# The plaintext message
message = "Sensitive Information"

# Encrypt the message
encrypted_message = encrypt_message(key, message)
print(f"Encrypted Message (hex): {encrypted_message.hex()}")

# Decrypt the message
decrypted_message = decrypt_message(key, encrypted_message)
print(f"Decrypted Message: {decrypted_message}")
