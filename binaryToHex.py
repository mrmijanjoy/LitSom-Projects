import hashlib
import os

def binaryToHex(file_path):
    hash_func = hashlib.sha3_256()
    with open(file_path, "rb") as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            hash_func.update(data)
    return hash_func.hexdigest()

def main():
    folder_path = 'task2'
    file_hashes = []

    # Calculate hashes for files
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            file_hash = binaryToHex(file_path)
            file_hashes.append(file_hash)

    # Sort file hashes
    sorted_hashes = sorted(file_hashes)

    # Combine sorted hashes into a single string
    combined_hash = ''.join(sorted_hashes)

    # Email
    email = 'mrmijanjoy@gmail.com'

    # Concatenate email in lowercase
    combined_string = combined_hash.lower() + email.lower()

    # Calculate SHA3-256 of the final string
    final_hash = hashlib.sha3_256(combined_string.encode('utf-8')).hexdigest()

    print(final_hash)

if __name__ == "__main__":
    main()
