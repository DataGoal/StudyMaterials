import re

import yaml


def convert_ddl(input_ddl, datatype_map):
    # Extract table name
    table_name_match = re.search(r'CREATE TABLE (\w+)', input_ddl)
    table_name = table_name_match.group(1) if table_name_match else ''
    print (table_name)

    # Extract column names, data types, and sizes from the input DDL
    matches = re.findall(r'(\w+)\s+(\w+)(?:\((\d+)\))?,?', input_ddl)[1:]
    print(matches[1:])

    # Convert data types using the mapping
    converted_columns = [
        f'{column} {datatype_map.get(data_type.lower(), data_type)}{"("}{size}{")"}'
        for column, data_type, size in matches
    ]
    print (converted_columns)

    # Construct the output DDL with parentheses around columns
    output_ddl = f'CREATE TABLE {table_name} ({", ".join(converted_columns)});'

    return output_ddl


def load_table(p_map, t_list):
    for t in t_list:
        if t in p_map:
            p_cols = p_map[t]
            print(f"{p_cols} - - Loading")
        else:
            print("Not Loading")


def process_values(input_string):
    # Assuming input_string is a comma-separated string
    values = input_string.split(',')

    # Now 'values' is a list containing individual values
    print(values)


def load_yaml_contenet(yaml_file_path):
    try:
        with open(yaml_file_path, 'r') as file:
            yaml_content = yaml.safe_load(file)
        return yaml_content
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        return None


# Example usage
comma_separated_values = "value1,value2,value3"
print(process_values(comma_separated_values))

load_table({"foo":"bar", "kal":"lak", "jav": "vaj"},["foo", "jav", "bal"])

# Input DDL
input_ddl = '''
CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);
'''

# Data type mapping
datatype_map = {
    'int': 'integer',
    'varchar': 'poda'
}

# Convert the DDL
output_ddl = convert_ddl(input_ddl, datatype_map)

# Print the result
print(load_table)
