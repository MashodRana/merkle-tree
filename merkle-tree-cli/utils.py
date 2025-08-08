import hashlib

buffer_size = 4096


def hashing_data(data):
    return hashlib.sha256(data).hexdigest()

def hash_file_content(file_path: str):
    hash_obj = hashlib.sha256()
    buffer = bytearray(buffer_size)

    with open(file_path, 'rb', buffering=0) as file:
        while True:
            bytes_read = file.readinto(buffer)
            if bytes_read == 0:
                break
            hash_obj.update(buffer[:bytes_read])
    return hash_obj.hexdigest()

file_path = "/home/mashod-rana/projects/personal/Merkle-tree/merkle-tree-cli/lib/hashing.js"
hashed_content = hash_file_content(file_path)
print(hashed_content)