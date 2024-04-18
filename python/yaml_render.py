import yaml

yaml_content = """
dir_config:
  environment: {{ env }}
  acc: {{ acc }}
"""

data_to_replace = {'env': 'dev', 'acc':'123'}

# Replace placeholders
for key, value in data_to_replace.items():
    yaml_content = yaml_content.replace(f'{{{{ {key} }}}}', value)

# Load YAML content after string replacement
parsed_yaml = yaml.safe_load(yaml_content)

# Write updated YAML to a new file
output_path = 'C:\\Users\\bbala\\Desktop\\BBC\\GIT\\StudyMaterials\\inputs\\file.yaml'
with open(output_path, 'w') as output_file:
    yaml.dump(parsed_yaml, output_file, default_flow_style=False)

print(f"YAML has been updated and written to {output_path}.")

import os
import shutil

input_directory = "/config"
output_directory = "/config_dev"

# Get a list of all files with the extension *.yaml in the input directory and its subdirectories
all_yaml_files = []
for root, dirs, files in os.walk(input_directory):
    for file in files:
        if file.endswith(".yaml"):
            file_path = os.path.join(root, file)
            all_yaml_files.append(file_path)

# Process and write each YAML file to the output directory
for input_yaml_file_path in all_yaml_files:
    # Create the output file path with the same structure under the output directory
    relative_path = os.path.relpath(input_yaml_file_path, start=input_directory)
    output_yaml_file_path = os.path.join(output_directory, relative_path)

    # Ensure the directory for the output file exists, create it if necessary
    os.makedirs(os.path.dirname(output_yaml_file_path), exist_ok=True)

    # Your processing logic goes here
    # For example, you can read the content of the input YAML file, perform some processing,
    # and then write the processed content to the output file.

    # Read the content of the input YAML file
    with open(input_yaml_file_path, 'r') as input_file:
        input_content = input_file.read()

    # Process the content (you can replace this with your specific processing logic)
    # For example, you can use the ruemal.yaml library for processing YAML content.
    processed_content = input_content.upper()

    # Write the processed content to the output YAML file
    with open(output_yaml_file_path, 'w') as output_file:
        output_file.write(processed_content)

    print(f"Processed '{input_yaml_file_path}' and wrote to '{output_yaml_file_path}' with the same directory structure.")

