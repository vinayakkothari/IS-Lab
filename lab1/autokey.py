def autokey_encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    
    # Convert key to a letter
    key_char = chr(key + ord('A'))
    
    # Prepare key stream
    key_stream = key_char + plaintext  # Autokey starts with the key and continues with the plaintext

    def char_to_num(c):
        return ord(c) - ord('A')

    def num_to_char(n):
        return chr(n + ord('A'))

    ciphertext = ""
    for i in range(len(plaintext)):
        p_num = char_to_num(plaintext[i])
        k_num = char_to_num(key_stream[i])
        c_num = (p_num + k_num) % 26
        ciphertext += num_to_char(c_num)
    
    return ciphertext

key = 7
message = "the house is being sold tonight"

encrypted_message = autokey_encrypt(message, key)
print("Encrypted message:", encrypted_message)
