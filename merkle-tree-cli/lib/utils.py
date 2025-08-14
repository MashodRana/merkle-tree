import hashlib
from pathlib import Path

buffer_size = 4096


def hash_data(data):
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


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


def get_files_of_directory(dir_path: str):
    dir_path = Path(dir_path)
    all_files = [f for f in dir_path.rglob("*") if f.is_file()]
    all_files.sort()
    return all_files


def write_output_to_file(file_path: str, data: dict):
    if not file_path.endswith(".json"):
        raise Exception("output file must be json file.")

    import json
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        raise Exception(f"File write error: {e}")
