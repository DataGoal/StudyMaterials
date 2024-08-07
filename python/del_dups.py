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

UPDATE eventmetadata.event_reference AS er
SET EXPRTN_DT = current_date,
    UPDT_TS = current_timestamp,
    UPDT_USER_CD = current_user
FROM eventmetadata.event_output_reference AS eor
JOIN eventmetadata.output_reference AS orf ON eor.output_id = orf.output_id
WHERE CURRENT_DATE BETWEEN er.EFF_DT AND er.EXPRTN_DT
  AND er.EVENT_ID = eor.EVENT_ID
  AND LOWER(orf.output_grp_nm) LIKE '%cog%';

import os

# Directory where the search starts
start_dir = '/etc/tmp'
# Output file where all contents will be appended
output_file = '/path/to/output_file.txt'

# Ensure the output file is empty before appending
with open(output_file, 'w') as f_out:
    f_out.write("")

# Walk through the directory structure
for root, dirs, files in os.walk(start_dir):
    for file in files:
        if file == 'col_info.txt':
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f_in:
                content = f_in.read()
                with open(output_file, 'a') as f_out:
                    f_out.write(content + "\n")

print("All contents have been appended to:", output_file)

