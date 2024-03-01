import os
import shutil
import filecmp

def copy_modified_files(src, dest):
    for root, dirs, files in os.walk(src):
        relative_path = os.path.relpath(root, src)
        destination_path = os.path.join(dest, relative_path)

        # Create directories if not exist in the destination
        os.makedirs(destination_path, exist_ok=True)

        for file in files:
            src_file_path = os.path.join(root, file)
            dest_file_path = os.path.join(destination_path, file)

            # Check if file exists and is modified
            if not os.path.exists(dest_file_path) or filecmp.cmp(src_file_path, dest_file_path) == False:
                shutil.copy2(src_file_path, dest_file_path)
                print(f"Copied: {src_file_path} to {dest_file_path}")

# Example usage
src_path = '/path/to/source'
dest_path = '/path/to/destination'

copy_modified_files(src_path, dest_path)
