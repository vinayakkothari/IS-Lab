from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import numpy as np

def print_state(state, title="State"):
    """Helper function to print the state matrix."""
    print(title)
    print(np.array(state).reshape(4, 4).tolist())

def aes_encrypt(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(message, AES.block_size))
    return ciphertext

# Define the key and message
key_hex = "FEDCBA9876543210FEDCBA9876543210"
key = bytes.fromhex(key_hex)
message = b"Top Secret Data"

# Perform AES encryption
ciphertext = aes_encrypt(message, key)
print(f"Ciphertext (hex): {ciphertext.hex()}")

# Since pycryptodome does not provide direct access to individual AES rounds,
# the following steps are demonstrated theoretically. Below is the conceptual outline:

print("\nKey Expansion (Conceptual):")
print("AES-192 key is expanded to 52 words (not displayed here).")

print("\nInitial Round:")
print("AddRoundKey (XOR with the first round key).")

print("\nMain Rounds (10 rounds):")
print("1. SubBytes: Substitute bytes using S-Box.")
print("2. ShiftRows: Shift rows of the state.")
print("3. MixColumns: Mix columns of the state.")
print("4. AddRoundKey: XOR with the round key.")

print("\nFinal Round (no MixColumns):")
print("1. SubBytes")
print("2. ShiftRows")
print("3. AddRoundKey")

# Note: The actual byte-by-byte transformations and key schedule are handled internally by pycryptodome.
