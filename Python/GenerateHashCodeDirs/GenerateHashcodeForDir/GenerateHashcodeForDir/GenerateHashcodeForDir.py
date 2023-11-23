
import hashlib
import os
from tqdm import tqdm

def generate_hash(file_path, hash_algorithm="sha256"):
    """
    Generate a hash for a file using the specified hash algorithm.
    :param file_path: Path to the file.
    :param hash_algorithm: Hash algorithm to use (e.g., "md5", "sha1", "sha256").
    :return: The hash value as a hexadecimal string.
    """
    if not os.path.isfile(file_path):
        return None

    hash_func = hashlib.new(hash_algorithm)
    with open(file_path, "rb") as file:
        while True:
            data = file.read(8192)  # Read the file in 8KB chunks
            if not data:
                break
            hash_func.update(data)

    return hash_func.hexdigest()

def generate_hashes_for_directory(directory_path, hash_algorithm="sha256"):
    """
    Generate hash codes for all files in a directory.
    :param directory_path: Path to the directory.
    :param hash_algorithm: Hash algorithm to use (e.g., "md5", "sha1", "sha256").
    :return: A dictionary with file paths as keys and hash codes as values.
    """
    hash_dict = {}
    for root, _, files in os.walk(directory_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = generate_hash(file_path, hash_algorithm)
            # print(f'{file_path=} {file_hash}')
            if file_hash is not None:
                hash_dict[file_path] = file_hash

    return hash_dict

if __name__ == "__main__":
    directory_path = "D:\VirtualBox"  # Replace with the path to your directory
    hash_algorithm = "sha256"  # You can change this to "md5" or "sha1" if needed

    hash_dict = generate_hashes_for_directory(directory_path, hash_algorithm)
    print(f'Done parsing the directory: {directory_path}')
    for file_path, hash_code in hash_dict.items():
        print(f"{file_path}: {hash_code}")