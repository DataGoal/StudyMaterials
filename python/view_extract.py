import re

with open("C:\\Users\\bbala\\Desktop\\BBC\\GIT\\StudyMaterials\\inputs\\input.txt", 'r') as infile, \
        open("C:\\Users\\bbala\\Desktop\\BBC\\GIT\\StudyMaterials\\inputs\\output_view.txt", 'w') as outfile:
    content = infile.read()
    views = re.findall(r'CREATE VIEW[^;]*;', content, re.DOTALL)

    for view in views:
        # Remove line breaks and extra spaces within the view definition
        view = ' '.join(view.split())
        outfile.write(view + '\n')

import re

# Function to extract schema and view names from a line
def extract_schema_view(line):
    match = re.match(r"CREATE VIEW (\w*\.\w*)", line)
    if match:
        return match.group(1)
    else:
        return None

# Input file path
input_file_path = "C:\\Users\\bbala\\Desktop\\BBC\\GIT\\StudyMaterials\\inputs\\output_view.txt"

# Output files
no_schema_file_path = "C:\\Users\\bbala\\Desktop\\BBC\\GIT\\StudyMaterials\\inputs\\no_schema.txt"
schema_files = {}

with open(input_file_path, "r") as input_file:
    for line in input_file:
        line = line.strip()
        if line.startswith("CREATE VIEW"):
            schema_view = extract_schema_view(line)
            if schema_view:
                schema, view = schema_view.split(".")
                # Create a file for the schema if it doesn't exist
                if schema not in schema_files:
                    schema_files[schema] = open(f"C:\\Users\\bbala\\Desktop\\BBC\\GIT\\StudyMaterials\\inputs\\{schema}.txt", "w")
                # Write the line to the appropriate schema file
                schema_files[schema].write(line + "\n")
            else:
                # Write the line to the no_schema_file
                with open(no_schema_file_path, "a") as no_schema_file:
                    no_schema_file.write(line + "\n")

# Close all schema files
for file in schema_files.values():
    file.close()

