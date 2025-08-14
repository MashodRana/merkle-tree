import argparse
from pathlib import Path

from lib.utils import get_files_of_directory, write_output_to_file
from lib.merkle_tree import build_merkle_tree


def main(dir_path: Path, output_file_name: str):
    files = get_files_of_directory(dir_path)
    built_tree = build_merkle_tree(files, is_file_paths=True)
    write_output_to_file(output_file_name, built_tree)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merkle Tree CLI Tool in Python.")
    parser.add_argument("-d", "--dir-path", type=Path,
                        help="Directory path to build Merkle Tree from the files in the directory.")
    parser.add_argument("-o", "--output-file", type=str, help="Output file path where Merkle Tree JSON will be saved.")
    parser.add_argument("-v", "--verify", type=Path, help="Verify a file is exist in the Merkle Tree.")

    args = parser.parse_args()

    main(dir_path=args.dir_path, output_file_name=args.output_file)
