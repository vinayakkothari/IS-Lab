plaintext = input("Enter your plaintext in lowercase: ")
enplain = list(plaintext)
# print(enplain)
deplain = enplain
# The reason for converting into a list is to change each instance separately and not all at once (abba->cbbc)
key = int(input("Enter your cipher key: "))
alphabet = "abcdefghijklmnopqrstuvwxyz"
# encrypt
for x in range(len(enplain)):
  # Find the index of the letter in alphabet
  i = alphabet.index(enplain[x].lower())
  enplain[x] = alphabet[(i + key)%26]
# Conversion back to string since this would show the elements of the list as separate items
enplain = "".join(enplain)
print("encrypted: " + enplain)

# decrypt
for y in range(len(deplain)):
  # Find the index of the letter in alphabet
  j = alphabet.index(deplain[y].lower())
  deplain[y] = alphabet[(j - key)%26]
# Conversion back to string since this would show the elements of the list as separate items
deplain = "".join(deplain)
print("decrypted: " + deplain)