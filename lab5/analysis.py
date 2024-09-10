import hashlib
import random
import string
import time

# Step 1: Generate random strings
def generate_random_strings(num_strings, length_range=(10, 50)):
    random_strings = []
    for _ in range(num_strings):
        length = random.randint(*length_range)
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        random_strings.append(random_string)
    return random_strings

# Step 2: Hashing functions and collision detection
def compute_hashes(strings, hash_function):
    hashes = {}
    collision_count = 0
    
    start_time = time.time()
    for s in strings:
        hash_obj = hash_function()
        hash_obj.update(s.encode())
        hash_digest = hash_obj.hexdigest()
        
        # Collision detection
        if hash_digest in hashes:
            print(f"Collision detected: {hashes[hash_digest]} and {s} produce the same hash!")
            collision_count += 1
        else:
            hashes[hash_digest] = s
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    return elapsed_time, collision_count

# Step 3: Experiment
def run_experiment(num_strings):
    random_strings = generate_random_strings(num_strings)

    # MD5
    print("\nMD5 Results:")
    md5_time, md5_collisions = compute_hashes(random_strings, hashlib.md5)
    print(f"MD5 Computation Time: {md5_time:.6f} seconds")
    print(f"MD5 Collisions: {md5_collisions}")
    
    # SHA-1
    print("\nSHA-1 Results:")
    sha1_time, sha1_collisions = compute_hashes(random_strings, hashlib.sha1)
    print(f"SHA-1 Computation Time: {sha1_time:.6f} seconds")
    print(f"SHA-1 Collisions: {sha1_collisions}")
    
    # SHA-256
    print("\nSHA-256 Results:")
    sha256_time, sha256_collisions = compute_hashes(random_strings, hashlib.sha256)
    print(f"SHA-256 Computation Time: {sha256_time:.6f} seconds")
    print(f"SHA-256 Collisions: {sha256_collisions}")

# Step 4: Run the experiment with a dataset of 50-100 strings
if __name__ == "__main__":
    num_strings = random.randint(50, 100)
    run_experiment(num_strings)
