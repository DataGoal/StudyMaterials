def process_file(input_file, output_file):
    unique_entries = set()

    with open(input_file, 'r') as input_file:
        lines = input_file.readlines()

    with open(output_file, 'w') as output_file:
        for line in lines:
            # Split the line by space and get the entry at the sixth index
            entry = line.split()[5]

            # Check if the entry is unique
            if entry not in unique_entries:
                # If unique, add it to the set and write the line to the output file
                unique_entries.add(entry)
                output_file.write(line)

# Replace 'input.txt' and 'output.txt' with your actual file names
input_file_path = 'C:\\Users\\bbala\\Desktop\\BBC\\GIT\\StudyMaterials\\inputs\\input.txt'
output_file_path = 'C:\\Users\\bbala\\Desktop\\BBC\\GIT\\StudyMaterials\\inputs\\output_2.csv'

process_file(input_file_path, output_file_path)
