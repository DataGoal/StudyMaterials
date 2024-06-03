def convert_queries_to_single_line(file_path, output_file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    single_line_queries = []
    current_query = []

    for line in lines:
        stripped_line = line.strip()
        if stripped_line.endswith(';'):
            current_query.append(stripped_line)
            single_line_query = ' '.join(current_query)
            formatted_query = f'spark.sql("""{single_line_query}");'
            single_line_queries.append(formatted_query)
            current_query = []
        else:
            current_query.append(stripped_line)

    with open(output_file_path, 'w') as output_file:
        for query in single_line_queries:
            output_file.write(query + '\n')

# Example usage:
file_path = 'path/to/your/file.txt'
output_file_path = 'path/to/your/output_file.txt'
convert_queries_to_single_line(file_path, output_file_path)
