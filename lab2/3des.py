from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad

def encrypt_message(key, plaintext):
    """Encrypts the plaintext message using Triple DES with the given key."""
    # Create a DES3 cipher object with the given key and ECB mode
    cipher = DES3.new(key, DES3.MODE_ECB)
    # Pad the plaintext to ensure it's a multiple of the block size
    padded_text = pad(plaintext.encode(), DES3.block_size)
    # Encrypt the padded plaintext
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext

def decrypt_message(key, ciphertext):
    """Decrypts the ciphertext message using Triple DES with the given key."""
    # Create a DES3 cipher object with the given key and ECB mode
    cipher = DES3.new(key, DES3.MODE_ECB)
    # Decrypt the ciphertext
    padded_plaintext = cipher.decrypt(ciphertext)
    # Remove the padding from the decrypted plaintext
    plaintext = unpad(padded_plaintext, DES3.block_size).decode()
    return plaintext

# Define the 48-byte key and use only the first 24 bytes for 3DES
key_hex = "1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF"
key = bytes.fromhex(key_hex)[:24]  # Extract the first 24 bytes for 3DES

# The message to be encrypted
message = "Classified Text"

# Encrypt the message
encrypted_message = encrypt_message(key, message)
print(f"Encrypted Message (hex): {encrypted_message.hex()}")

# Decrypt the message
decrypted_message = decrypt_message(key, encrypted_message)
print(f"Decrypted Message: {decrypted_message}")
