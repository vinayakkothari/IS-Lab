def encrypt(text,s):
    result = ""
    
    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)

        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

def decrypt(cipher, s):
    result = ""
    
    for i in range(len(cipher)):
        char = cipher[i]
        if (char.isupper()):
            result += chr((ord(char) - (s-65)) % 26 + 65)

        else:
            result += chr((ord(char) - (s - 97)) % 26 + 97)
        
    return result
cipher = "XVIEWYWI"
s = 4
print ("cipher  : " + cipher)
print ("Shift : " + str(s))
print ("text: " + decrypt(cipher,s))