import random
import math

primes = []

public_key = None
private_key = None
n = None

def primefiller():
    limit = 1000
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit, i):
                sieve[j] = False
                
    for i in range(limit):
        if sieve[i]:
            primes.append(i)

def pickrandomprime():
    return random.choice(primes)

def setkeys():
    global public_key, private_key, n
    prime1 = pickrandomprime()
    prime2 = pickrandomprime()
    
    # Ensure prime1 != prime2
    while prime1 == prime2:
        prime2 = pickrandomprime()
    
    n = prime1 * prime2
    fi = (prime1 - 1) * (prime2 - 1)
    
    e = 3
    while math.gcd(e, fi) != 1:
        e += 2  # Use only odd e to avoid even numbers
    
    d = 1
    while (d * e) % fi != 1:
        d += 1
    
    public_key = (e, n)
    private_key = (d, n)

def modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if (exponent % 2) == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def encrypt(message):
    e, n = public_key
    return modular_exponentiation(message, e, n)

def decrypt(encrypted_text):
    d, n = private_key
    return modular_exponentiation(encrypted_text, d, n)

def encoder(message):
    return [encrypt(ord(letter)) for letter in message]

def decoder(encoded):
    return ''.join(chr(decrypt(num)) for num in encoded)

if __name__ == '__main__':
    primefiller()
    setkeys()
    print("Public key: ", public_key)
    print("Private key: ", private_key)
    message = input("Enter the message\n")
    coded = encoder(message)
    
    print("Initial message:")
    print(message)
    print("\n\nThe encoded message\n")
    print(' '.join(str(p) for p in coded))
    print("\n\nThe decoded message\n")
    print(decoder(coded))