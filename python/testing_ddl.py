# Assuming you have a file named 'your_file.txt'

file_path = 'C:\\Users\\bbala\\Downloads\\input_ddl.txt'
# Assuming you have a file named 'your_file.txt'

ddl_start_marker = "-- DDL Statements for Table \"STAGE\""
delimiter = '-----------'

with open(file_path, 'r') as file:
    print_lines = False
    skip_next_line = False

    for line in file:
        if skip_next_line:
            skip_next_line = False
            continue

        if line.startswith(ddl_start_marker):
            print_lines = True
            skip_next_line = True
            print(line, end='')  # Print the current line
        elif delimiter in line:
            print(line, end='')  # Print the delimiter line
            print_lines = False  # Stop printing until the next '-- DDL Statements for Table "STAGE"'
        elif print_lines:
            print(line, end='')  # Print the following lines until the delimiter is encountered
        else:
            continue

def process_ddl_statements(input_file, output_file):
    ddl_start_marker = "-- DDL Statements for Table \"STAGE\""
    delimiter = '-----------'
    print_lines = False
    skip_next_line = False

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if skip_next_line:
                skip_next_line = False
                continue

            if line.startswith(ddl_start_marker):
                print_lines = True
                skip_next_line = True
                outfile.write(line)  # Print the current line
            elif delimiter in line:
                #outfile.write(line)  # Print the delimiter line
                print_lines = False  # Stop printing until the next '-- DDL Statements for Table "STAGE"'
            elif print_lines:
                outfile.write(line)  # Print the following lines until the delimiter is encountered
            else:
                continue

def process_ddl_statements(input_file, output_file):
    start_pattern = "-- DDL Statements for Table \"STAGE\""
    end_pattern = '-----------'
    needed_lines = False

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.startswith(start_pattern):
                needed_lines = True
                outfile.write(line)  # Print the current line
            elif end_pattern in line:
                needed_lines = False  # Stop printing until the next '-- DDL Statements for Table "STAGE"'
            elif print_lines:
                outfile.write(line)  # Print the following lines until the delimiter is encountered
            else:
                continue

# Example usage:
input_filename = 'C:\\Users\\bbala\\Downloads\\input_ddl.txt'
output_filename = 'C:\\Users\\bbala\\Downloads\\out_ddl3.txt'
process_ddl_statements(input_filename, output_filename)

