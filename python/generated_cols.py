import re

# Define a regular expression pattern to match the table name and generated column
pattern = re.compile(r'CREATE TABLE (\w+) \((.+)\)')

# Open the input file
with open("C:\\Users\\bbala\\Desktop\\BBC\\GIT\\StudyMaterials\\inputs\\input.txt", "r") as file:
    # Read each line of the file
    for line in file:
        # Use regex to match the pattern in the line
        match = pattern.match(line)
        if match:
            table_name = match.group(1)
            column_defs = match.group(2)

            # Split the column definitions by comma and check for generated columns
            for column_def in column_defs.split(','):
                column_def = column_def.strip()  # Remove leading/trailing whitespace
                if "generated" in column_def:
                    column_name = column_def.split()[0]  # Extract column name
                    print(f"{table_name}, {column_name}")
