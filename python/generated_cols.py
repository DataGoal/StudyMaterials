import re

def extract_generated_columns(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            # Extract table name
            table_match = re.match(r'^CREATE TABLE IF NOT EXISTS (\w+)\(', line)
            if table_match:
                table_name = table_match.group(1)
                generated_columns = []

                # Extract generated columns
                columns = re.findall(r'(\w+)\s+\w+\s+generated always as identity', line)
                generated_columns.extend(columns)

                if generated_columns:
                    print(f"{table_name}, {', '.join(generated_columns)}")

# Usage
input_file = "C:\\Users\\bbala\\Desktop\\BBC\\GIT\\StudyMaterials\\inputs\\input.txt"
extract_generated_columns(input_file)

