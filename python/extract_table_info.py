import re
import csv

def extract_table_info(sql_string):
    # Extract table name
    table_name_match = re.search(r'CREATE TABLE (\w+)', sql_string)
    if table_name_match:
        table_name = table_name_match.group(1)
    else:
        raise ValueError("Table name not found in the SQL string")

    # Use provided logic to find content between the first and last parentheses
    start_index = sql_string.find('(')
    end_index = sql_string.rfind(')')

    # Extract the content between the first and last parentheses
    if start_index != -1 and end_index != -1 and start_index < end_index:
        columns_info_str = sql_string[start_index + 1:end_index].strip()
    else:
        raise ValueError("Column information not found in the SQL string")

    # Extract column details with simplified output
    column_details = re.findall(r'(\w+)\s+(\w+)(?:\(([^)]*)\))?\s*([^,]+)?(?:,|$)', columns_info_str)

    # Process and return the extracted information
    result = []
    for column_info in column_details:
        column_name, data_type, size, constraints = column_info

        # Default size to empty if not present
        size = f"({size})" if size else ""

        # Check if "NOT NULL" is present, default to "NULL" otherwise
        nullable = "NOT NULL" if "NOT NULL" in constraints else "NULL"

        # Append the formatted output to the result list
        result.append([table_name, column_name, data_type + size, nullable])

    return result

def process_sql_file(input_file, output_file):
    with open(input_file, 'r') as f:
        sql_content = f.read()

    # Split SQL statements based on semicolon
    sql_statements = sql_content.split(';')

    # Process each SQL statement and accumulate the results
    results = []
    for sql_statement in sql_statements:
        if sql_statement.strip():  # Skip empty statements
            results.extend(extract_table_info(sql_statement))

    # Write results to CSV file
    with open(output_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write header
        csv_writer.writerow(['Table Name', 'Column Name', 'Data Type', 'Nullable'])
        # Write data
        csv_writer.writerows(results)

# Example usage
input_file_path = 'C:\\Users\\bbala\\Desktop\\BBC\\GIT\\StudyMaterials\\inputs\\input.txt'
output_file_path = 'C:\\Users\\bbala\\Desktop\\BBC\\GIT\\StudyMaterials\\inputs\\output.csv'
process_sql_file(input_file_path, output_file_path)
