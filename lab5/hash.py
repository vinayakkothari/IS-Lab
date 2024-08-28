def custom_hash(input_string):
    hash_value = 5381
    for char in input_string:
        hash_value = ((hash_value << 5) + hash_value) + ord(char)
        hash_value &= 0xFFFFFFFF
    
    return hash_value
input_string = input("Enter string: ")
print(f"The hash value for '{input_string}' is: {custom_hash(input_string)}")
