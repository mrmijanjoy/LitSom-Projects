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


folder_path = 'task2'

file_hashes = []

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        file_hash = binaryToHex(file_path)
        file_hashes.append(file_hash)

sorted_hashes = sorted(file_hashes)
combined_hash = ''.join(sorted_hashes)
final_hex_code = combined_hash[:64]
print(final_hex_code)
