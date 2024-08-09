import pandas as pd
import yaml

# Define the input Excel file path
excel_file = "input.xlsx"

# Define the sheet names
environments = ["dev", "sit", "prd"]

# Initialize a dictionary to hold the data for all environments
output_dict = {}

# Iterate over each environment, read the respective sheet, and collect the data
for sheet_name in environments:
    # Read the Excel sheet into a DataFrame
    df = pd.read_excel(excel_file, sheet_name=sheet_name)

    # Initialize an empty list to hold the table data for the current environment
    table_list = []

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Create a dictionary for each table
        table_dict = {}
        table_name = row['Table Name']
        table_dict[table_name] = []

        # Parse the 'Select' groups
        if pd.notna(row['Select']):
            select_groups = row['Select'].split(' | ')
            table_dict[table_name].append({'select': select_groups})

        # Parse the 'Modify' groups
        if pd.notna(row['Modify']):
            modify_groups = row['Modify'].split(' | ')
            table_dict[table_name].append({'modify': modify_groups})

        # Parse the 'All_Privileges' groups
        if pd.notna(row['All_Privileges']):
            all_privilege_groups = row['All_Privileges'].split(' | ')
            table_dict[table_name].append({'all_privileage': all_privilege_groups})

        # Add the table dictionary to the table list
        table_list.append(table_dict)

    # Add the table list to the output dictionary under the current environment tag
    output_dict[sheet_name] = {'table_list': table_list}

# Write the entire output dictionary to a single YAML file
yaml_file = "combined_output.yaml"
with open(yaml_file, 'w') as file:
    yaml.dump(output_dict, file, default_flow_style=False)

print(f"Combined YAML output has been written to {yaml_file}")
