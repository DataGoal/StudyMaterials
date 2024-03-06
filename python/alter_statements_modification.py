import re

def generate_alter_statements_from_file(file_path):
    output_statements = []

    with open(file_path, 'r') as file:
        for line in file:
            statement = line.strip()
            match = re.match(r"ALTER TABLE (\w+) ADD CONSTRAINT \w+ PRIMARY KEY\((.+)\);", statement)
            if match:
                table_name = match.group(1)
                columns = [col.strip() for col in match.group(2).split(',')]
                for column in columns:
                    output_statements.append(f'ALTER TABLE {table_name} ALTER COLUMN {column} SET NOT NULL;')

    return output_statements

# Example usage:
file_path = 'path/to/your/input/file.txt'
output_statements = generate_alter_statements_from_file(file_path)

for output_statement in output_statements:
    print(output_statement)
