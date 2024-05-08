def extract_create_view_queries(file_path, output_file):
    with open(file_path, 'r') as file:
        with open(output_file, 'w') as out_file:
            query = ''
            inside_query = False
            for line in file:
                line = line.strip()
                if line.startswith('CREATE VIEW'):
                    inside_query = True
                    query = line
                elif inside_query:
                    query += ' ' + line
                    if line.endswith(';'):
                        out_file.write(query + '\n')
                        inside_query = False

# Example usage
input_file_path = 'your_input_file_path_here.txt'
output_file_path = 'your_output_file_path_here.txt'
extract_create_view_queries(input_file_path, output_file_path)
