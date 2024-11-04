import hashlib

# Function to create text files with specified content
def create_files():
    # Original message with at least 30 words
    message1 = """This is the original message that contains more than thirty words for the purpose of testing the hash 
    function and observing the avalanche effect. Even small changes in this text should result in a completely 
    different hash."""

    # Identical copy of the original message for file2
    message2 = message1  # file2 will be identical to file1

    # Slightly modified message for file3 (e.g., one word changed)
    message3 = """This is the original message that contains more than thirty words for the purpose of testing the hash 
    function and observing the avalanche effect. Even small changes in this text may lead to a completely 
    different hash."""  # Minor change in the text

    # Write contents to files
    with open('file1.txt', 'w') as f1:
        f1.write(message1)

    with open('file2.txt', 'w') as f2:
        f2.write(message2)

    with open('file3.txt', 'w') as f3:
        f3.write(message3)


# Function to generate hash of a file's contents
def generate_hash(file_path):
    hasher = hashlib.sha256()  # Using SHA-256 for hashing
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()


# Function to compare hash values of two files
def compare_hashes(hash1, hash2):
    return hash1 == hash2


# Main program execution
create_files()  # Create the text files with specified content

# Paths to text files
file1_path = 'file1.txt'
file2_path = 'file2.txt'
file3_path = 'file3.txt'

# Generate hashes for the three files
hash_file1 = generate_hash(file1_path)
hash_file2 = generate_hash(file2_path)
hash_file3 = generate_hash(file3_path)

# Output hashes
print(f"Hash of file1.txt: {hash_file1}")
print(f"Hash of file2.txt: {hash_file2}")
print(f"Hash of file3.txt: {hash_file3}")

# Check if hashes of file1 and file2 are identical
print("\nComparing file1 and file2:")
if compare_hashes(hash_file1, hash_file2):
    print("file1 and file2 are identical (hashes match).")
else:
    print("file1 and file2 are different (hashes do not match).")

# Check if hashes of file1 and file3 are identical
print("\nComparing file1 and file3:")
if compare_hashes(hash_file1, hash_file3):
    print("file1 and file3 are identical (hashes match).")
else:
    print("file1 and file3 are different (hashes do not match).")

# Check if hashes of file2 and file3 are identical
print("\nComparing file2 and file3:")
if compare_hashes(hash_file2, hash_file3):
    print("file2 and file3 are identical (hashes match).")
else:
    print("file2 and file3 are different (hashes do not match).")

# Observing the avalanche effect
print("\nAvalanche Effect Observation:")
print(f"Hash Difference between file1 and file3:\n{hash_file1}\n{hash_file3}")
print(f"Hash Difference between file2 and file3:\n{hash_file2}\n{hash_file3}")

