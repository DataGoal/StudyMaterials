# Extract columns with "WITH DEFAULT" clause and their default values
def sample(input_string):
    # Extract schema and table name from CREATE statement
    schema_table_info = input_string.split('TABLE')[1].strip().strip('"')
    print(schema_table_info)
    schema, table_name = schema_table_info.split('.')

    columns_with_default = [col.strip() for col in input_string.split('\n') if 'WITH DEFAULT' in col]
    alter_table_statements = []

    # Generate ALTER TABLE statements
    for col_with_default in columns_with_default:
        col_name = col_with_default.split()[0].strip('""')
        default_value = col_with_default.split('WITH DEFAULT')[1].replace('\'', '').strip(',').strip(' ')
        alter_statement = f'ALTER TABLE "{schema}"."{table_name}" ALTER COLUMN {col_name} SET DEFAULT "{default_value}";'
        alter_table_statements.append(alter_statement)

    return alter_table_statements

# Specify the path to your SQL file
file_path = 'C:\\Users\\bbala\\Desktop\\BBC\\GIT\\StudyMaterials\\inputs\\input.txt'
output_file = 'C:\\Users\\bbala\\Desktop\\BBC\\GIT\\StudyMaterials\\inputs\\alter.txt'

def process_input_file(file_path, output_file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Split content into statements using 'CREATE TABLE' as a delimiter
    raw_statements = content.split('CREATE')[1:]

    # Process each statement using the extract_between_create_and_semicolon function
    statements = [statement for statement in raw_statements if 'TABLE' in statement]
    alter_statements = [sample(statement) for statement in statements]

    # Flatten the list of lists
    alter_statements = [item for sublist in alter_statements for item in sublist]

    with open(output_file_path, 'w') as output_file:
        for statement in alter_statements:
            output_file.write(statement + '\n')

process_input_file(file_path, output_file)
