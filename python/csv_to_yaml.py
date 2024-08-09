import pandas as pd
import yaml


def excel_to_yaml(input_file, output_file):
    # Define the sheet names (environments)
    environments = ["dev", "sit", "prd"]

    # Initialize a dictionary to hold the data for all environments
    output_dict = {}

    # Iterate over each environment, read the respective sheet, and collect the data
    for sheet_name in environments:
        # Read the Excel sheet into a DataFrame
        df = pd.read_excel(input_file, sheet_name=sheet_name)

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

    # Write the entire output dictionary to a YAML file
    with open(output_file, 'w') as file:
        yaml.dump(output_dict, file, default_flow_style=False)

    print(f"Combined YAML output has been written to {output_file}")

# Example usage
# excel_to_yaml('input.xlsx', 'combined_output.yaml')

import pandas as pd
import yaml


def yaml_to_excel(input_file, output_file):
    # Read the YAML file
    with open(input_file, 'r') as file:
        data = yaml.safe_load(file)

    # Prepare a dictionary to hold DataFrames for each sheet
    sheets = {}

    # Process each environment in the YAML data
    for environment, content in data.items():
        table_list = content['table_list']
        rows = []

        # Process each table
        for table in table_list:
            table_name, permissions = list(table.items())[0]

            # Prepare rows for the current table
            for permission in permissions:
                for perm_type, groups in permission.items():
                    row = {
                        'Table Name': table_name,
                        'Select': '',
                        'Modify': '',
                        'All_Privileges': ''
                    }

                    if perm_type == 'select':
                        row['Select'] = ' | '.join(groups)
                    elif perm_type == 'modify':
                        row['Modify'] = ' | '.join(groups)
                    elif perm_type == 'all_privileage':
                        row['All_Privileges'] = ' | '.join(groups)

                    rows.append(row)

        # Convert the rows to a DataFrame
        df = pd.DataFrame(rows)
        sheets[environment] = df

    # Write each DataFrame to a separate sheet in the Excel file
    with pd.ExcelWriter(output_file) as writer:
        for sheet_name, df in sheets.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"Excel file has been written to {output_file}")

# Example usage
# yaml_to_excel('combined_output.yaml', 'output.xlsx')

import yaml
from pyspark.sql import SparkSession


def apply_grants_from_yaml(yaml_file, spark: SparkSession):
    # Read the YAML file
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)

    # Initialize a list to collect SQL statements
    sql_statements = []

    # Process each environment in the YAML data
    for environment, content in data.items():
        table_list = content['table_list']

        # Process each table
        for table in table_list:
            table_name, permissions = list(table.items())[0]

            # Generate GRANT statements
            for permission in permissions:
                for perm_type, groups in permission.items():
                    for group in groups:
                        if perm_type == 'select':
                            sql_statements.append(f"GRANT SELECT ON TABLE {table_name} TO {group};")
                        elif perm_type == 'modify':
                            sql_statements.append(f"GRANT MODIFY ON TABLE {table_name} TO {group};")
                        elif perm_type == 'all_privileage':
                            sql_statements.append(f"GRANT ALL PRIVILEGE ON TABLE {table_name} TO {group};")

    # Execute all SQL statements in a batch
    try:
        for sql in sql_statements:
            print(f"Executing: {sql}")  # For debugging, remove in production
            spark.sql(sql)
        print("All grants applied successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
# Create a Spark session
spark = SparkSession.builder \
    .appName("Grant Permissions") \
    .getOrCreate()

# Apply grants from YAML
apply_grants_from_yaml('combined_output.yaml', spark)
