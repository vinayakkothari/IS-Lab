def char_to_num(c):
    return ord(c) - ord('A')

def num_to_char(n):
    return chr(n + ord('A'))

def prepare_message(message):
    message = message.replace(" ", "").upper()
    if len(message) % 2 != 0:
        message += 'X'  # Padding with 'X' if length is odd
    return message

def hill_cipher_encrypt(message, key_matrix):
    def matrix_mult_mod26(A, B):
        """ Multiplies two matrices A and B under modulo 26 """
        rows_A, cols_A = len(A), len(A[0])
        rows_B, cols_B = len(B), len(B[0])
        
        assert cols_A == rows_B, "Incompatible matrices for multiplication"
        
        # Initialize result matrix with zeros
        result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
        
        # Matrix multiplication
        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % 26
        return result

    # Convert the message into pairs
    pairs = [message[i:i+2] for i in range(0, len(message), 2)]
    
    encrypted_message = ""
    for pair in pairs:
        # Convert pair to numbers
        pair_nums = [char_to_num(pair[0]), char_to_num(pair[1])]
        
        # Convert pair to matrix form
        pair_matrix = [[pair_nums[0]], [pair_nums[1]]]
        
        # Encrypt using matrix multiplication
        encrypted_matrix = matrix_mult_mod26(key_matrix, pair_matrix)
        
        # Convert numbers back to characters
        encrypted_message += num_to_char(encrypted_matrix[0][0]) + num_to_char(encrypted_matrix[1][0])
    
    return encrypted_message

# Key matrix (2x2)
key_matrix = [[3, 3], [2, 7]]

message = "We live in an insecure world"
# message = input("Enter plaintext")

prepared_message = prepare_message(message)

encrypted_message = hill_cipher_encrypt(prepared_message, key_matrix)

print("Encrypted message:", encrypted_message)