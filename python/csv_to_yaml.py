import csv
import yaml

# Define the input CSV file path
csv_file = "C:\\Users\\bbala\\Desktop\\BBC\\GIT\\StudyMaterials\\inputs\\access_control.csv"

# Initialize an empty list to hold the table data
table_list = []

# Read the CSV file
with open(csv_file, mode='r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        # Create a dictionary for each table
        table_dict = {}
        table_name = row['Table Name']
        table_dict[table_name] = []

        # Parse the 'Select' groups
        if row['Select']:
            select_groups = row['Select'].split(' | ')
            table_dict[table_name].append({'select': select_groups})

        # Parse the 'Modify' groups
        if row['Modify']:
            modify_groups = row['Modify'].split(' | ')
            table_dict[table_name].append({'modify': modify_groups})

        # Parse the 'All_Privileges' groups
        if row['All_Privileges']:
            all_privilege_groups = row['All_Privileges'].split(' | ')
            table_dict[table_name].append({'all_privileage': all_privilege_groups})

        # Add the table dictionary to the table list
        table_list.append(table_dict)

# Convert the list to a dictionary under the key 'table_list'
output_dict = {'table_list': table_list}

# Output the dictionary as YAML
yaml_output = yaml.dump(output_dict, default_flow_style=False)

# Print the YAML output or write to a file
print(yaml_output)

# Optionally, write to a YAML file
with open('output.yaml', 'w') as yaml_file:
    yaml.dump(output_dict, yaml_file, default_flow_style=False)
