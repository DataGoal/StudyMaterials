#import re
input_file_path = 'C:\\Users\\bbala\\Desktop\\BBC\\GIT\\StudyMaterials\\inputs\\input.txt'
output_file_path = 'C:\\Users\\bbala\\Desktop\\BBC\\GIT\\StudyMaterials\\inputs\\out3.txt'
def extract_between_first_last_parentheses(input_string):
    # Find the first and last occurrences of parentheses
    start_index = input_string.find('(')
    end_index = input_string.rfind(')')

    # Extract the content between the first and last parentheses
    if start_index != -1 and end_index != -1 and start_index < end_index:
        result = input_string[:start_index].strip() + '(' + input_string[start_index + 1:end_index].strip() + ');'
        result1 = result.replace(' OCET', '')
        result2 = result1.split(',')
        result3 = [col[:col.find(' WITH DEFAULT')].strip() if 'WITH DEFAULT' in col else col.strip() for col in
                            result2]
        new_statement = ', '.join(result3) + ');'
        return new_statement
    else:
        return None

# Example usage
original_statement = 'CREATE TABLE "stage"."cus_table"("FIRST_NAME" VARCHAR(255 OCET) NOT NULL, "LAST_NAME" VARCHAR(25 OCET) NOT NULL, "AGE" INTEGER NOT NULL, "GENDER" CHAR(1 OCET) NOT NULL WITH DEFAULT "M", "SEX" CHAR(1 OCET) NOT NULL WITH DEFAULT "F", "TEST" VARCHAR(22 OCET) NOT NULL WITH DEFAULT "Yes", "DT" TIMESTAMP NOT NULL WITH DEFAULT CURRENT TIMESTAMP) ORGANIZED ROW;'

content_between_first_last_parentheses = extract_between_first_last_parentheses(original_statement)
# print(content_between_first_last_parentheses)

def extract_between_create_and_semicolon(input_string):
    start_index = input_string.find('CREATE')
    end_index = input_string.find(';')

    if start_index != -1 and end_index != -1 and start_index < end_index:
        return input_string[start_index:end_index + 1].strip()
    else:
        return None

def process_input_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Split content into statements using 'CREATE TABLE' as a delimiter
    raw_statements = content.split('CREATE')[1:]

    # Process each statement using the extract_between_create_and_semicolon function
    statements = [extract_between_create_and_semicolon('CREATE' + statement) for statement in raw_statements]

    # Filter out None values
    statements = list(filter(None, statements))

    with open(output_file_path, 'w') as output_file:
        for statement in statements:
            output_file.write(extract_between_first_last_parentheses(statement) + '\n')

# Example usage:
process_input_file('C:\\Users\\bbala\\Desktop\\BBC\\GIT\\StudyMaterials\\inputs\\input.txt')


# Example usage
input_file_path = 'C:\\Users\\bbala\\Desktop\\BBC\\GIT\\StudyMaterials\\inputs\\input.txt'
output_file_path = 'C:\\Users\\bbala\\Desktop\\BBC\\GIT\\StudyMaterials\\inputs\\out.txt'

