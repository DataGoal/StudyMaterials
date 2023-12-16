# Sample input SQL statement


# Extract columns with "WITH DEFAULT" clause and their default values
def sample(input_string):
    columns_with_default = [col.strip() for col in input_string.split('\n') if 'WITH DEFAULT' in col]
    alter_table_statements = []

# Generate ALTER TABLE statements
    for col_with_default in columns_with_default:
        col_name = col_with_default.split()[0].strip('""')
        default_value = col_with_default.split('WITH DEFAULT')[1].replace('\'','').strip(',').strip(' ')
        alter_statement = f'ALTER TABLE dbname.tabname ALTER COLUMN {col_name} SET DEFAULT "{default_value}";'
        alter_table_statements.append(alter_statement)

    return alter_table_statements

# Specify the path to your SQL file
file_path = 'C:\\Users\\bbala\\Desktop\\BBC\\GIT\\StudyMaterials\\inputs\\input.txt'
output_file = 'C:\\Users\\bbala\\Desktop\\BBC\\GIT\\StudyMaterials\\inputs\\alter.txt'
def process_input_file(file_path,output_file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Split content into statements using 'CREATE TABLE' as a delimiter
    raw_statements = content.split('CREATE')[1:]
    print (raw_statements)

    # Process each statement using the extract_between_create_and_semicolon function
    statements = [sample('CREATE' + statement) for statement in raw_statements]

    # Filter out None values
    statements = list(filter(None, statements))

    with open(output_file_path, 'w') as output_file:
        for statement in statements:
            output_file.write(sample(statement) + '\n')

process_input_file(file_path, output_file)