import re

def extract_lines_from_file(file_path):
    pattern = re.compile(r'^val.*\[\]$')
    result = []

    with open(file_path, 'r') as file:
        lines = file.readlines()
        result = [line.strip() for line in lines if pattern.match(line.strip())]

    return result

# Example usage:
file_path = 'your_file.txt'  # Replace with the path to your file
result = extract_lines_from_file(file_path)

for line in result:
    print(line)
