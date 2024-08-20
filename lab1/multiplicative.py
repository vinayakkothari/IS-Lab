def encrypt(plain_text, key):
    cipher_text = ""
    for char in plain_text:
            char = char.upper()
            # Apply the multiplicative cipher formula
            encrypted_char = chr(((ord(char) - ord('A')) * key) % 26
                                 + ord('A'))
            cipher_text += encrypted_char
    return cipher_text

def decrypt(cipher_text, key):
    plain_text = ""
    # Calculate the modular multiplicative inverse of the key
    key_inverse = pow(key, -1, 26)
    for char in cipher_text:
            char = char.upper()
            # Apply the multiplicative cipher decryption formula
            decrypted_char = chr(((ord(char) - ord('A')) * key_inverse) 
                                 % 26 + ord('A'))
            plain_text += decrypted_char
    return plain_text

plain_text = input("Enter text: ")
key = int(input("key: "))

# Encryption
cipher_text = encrypt(plain_text, key)
print("Encrypted:", cipher_text)

# Decryption
decrypted_text = decrypt(cipher_text, key)
print("Decrypted:", decrypted_text)
