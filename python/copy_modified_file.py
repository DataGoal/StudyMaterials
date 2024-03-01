import os
import shutil

def copy_modified_files(source, destination):
    for root, dirs, files in os.walk(source):
        for file in files:
            source_path = os.path.join(root, file)
            relative_path = os.path.relpath(source_path, source)
            destination_path = os.path.join(destination, relative_path)

            # Check if the file in the source has been modified or does not exist in the destination
            if not os.path.exists(destination_path) or os.path.getmtime(source_path) > os.path.getmtime(destination_path):
                shutil.copy2(source_path, destination_path)
                print(f"Copied: {relative_path}")

# Source directory to copy
source_directory = "/path/to/source_directory"

# Destination directory
destination_directory = "/path/to/destination_directory"

# Copy only modified files
copy_modified_files(source_directory, destination_directory)
