import json

import os


def create_folders_and_files(structure, parent_folder):
    for key, value in structure.items():
        path = os.path.join(parent_folder, key)
        if value:
            os.makedirs(path)
            create_folders_and_files(value, path)
        else:
            if '.' in key:
                open(path, "a").close()
            else:
                os.makedirs(path)


def generate_folder_structure(root_folder, json_file_path):
    # Dictionary containing the folder structure
    with open(json_file_path, "r") as f:
        structure = json.load(f)

    # Create the root folder
    if not os.path.exists(root_folder):
        os.makedirs(root_folder)

    # Recursively create the folders and files in the structure

    create_folders_and_files(structure, root_folder)


def main():
    import argparse

    # Parse the command line arguments
    parser = argparse.ArgumentParser(
        description="Generate a folder structure for machine learning/deep learning projects")
    parser.add_argument("root_folder", type=str, help="The root folder path")
    args = parser.parse_args()

    # Generate the folder structure
    json_file_path = "mlskeleton/folder_structure.json"
    generate_folder_structure(args.root_folder, json_file_path=json_file_path)


if __name__ == "__main__":
    main()
