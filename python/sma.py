import re

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
print(output_ddl)
