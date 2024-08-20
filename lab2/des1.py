from Crypto.Cipher import DES
import binascii

def pad_message(message):
    while len(message) % 8 != 0:
        message += ' '
    return message

# Encryption
def encrypt_message(message, key):
    des = DES.new(key.encode(), DES.MODE_ECB)
    padded_message = pad_message(message)
    encrypted_message = des.encrypt(padded_message.encode())
    return binascii.hexlify(encrypted_message).decode()

# Decryption
def decrypt_message(encrypted_message, key):
    des = DES.new(key.encode(), DES.MODE_ECB)
    decrypted_message = des.decrypt(binascii.unhexlify(encrypted_message.encode()))
    return decrypted_message.decode().strip()

# Original message and key
message = "Confidential Data"
key = "A1B2C3D4"

encrypted_message = encrypt_message(message, key)
print(f"Encrypted Message: {encrypted_message}")

decrypted_message = decrypt_message(encrypted_message, key)
print(f"Decrypted Message: {decrypted_message}")
