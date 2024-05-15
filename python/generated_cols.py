import re

def extract_generated_columns(input_file):
    generated_columns = []
    with open(input_file, 'r') as file:
        for line in file:
            match = re.search(r'CREATE TABLE (\w+) \((.*?)\)', line)
            if match:
                table_name = match.group(1)
                columns = match.group(2).split(',')
                for column in columns:
                    if 'generated always as identity' in column:
                        column_name = re.search(r'(\w+)\s', column).group(1)
                        generated_columns.append((table_name.strip(), column_name.strip()))
    return generated_columns

input_file = "C:\\Users\\bbala\\Desktop\\BBC\\GIT\\StudyMaterials\\inputs\\input.txt"
generated_columns = extract_generated_columns(input_file)

for table, column in generated_columns:
    print(table + ",", column)

