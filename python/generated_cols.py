import re

def extract_generated_columns(input_file):
    generated_columns = []
    with open(input_file, 'r') as file:
        for line in file:
            match = re.search(r'CREATE TABLE IF NOT EXISTS (\w+)\((.*?)\);', line)
            if match:
                table_name = match.group(1)
                column_definitions = match.group(2).split(',')
                for column_def in column_definitions:
                    if 'generated always as identity' in column_def:
                        column_name = re.search(r'(\w+)\s.*?generated always as identity', column_def).group(1)
                        generated_columns.append((table_name.strip(), column_name.strip()))
    return generated_columns

input_file = "C:\\Users\\bbala\\Desktop\\BBC\\GIT\\StudyMaterials\\inputs\\input.txt"
generated_columns = extract_generated_columns(input_file)

for column in generated_columns:
    print(column[0] + ', ' + column[1])