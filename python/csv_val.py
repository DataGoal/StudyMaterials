import pandas as pd

# Read the CSV file
df = pd.read_csv('C:\\Users\\bbala\\Desktop\\BBC\\GIT\\StudyMaterials\\inputs\\checking.csv', header=None, names=['Name', 'Value'])

# Create a function to validate and concatenate values
def validate_and_concat(values):
    return 'validate' + '_'.join(map(str, values))

# Initialize an empty dictionary to store results
result_dict = {}

# Iterate through the DataFrame
for row in df.itertuples(index=False):
    name = row.Name
    value = row.Value

    # If the name is not in the dictionary, initialize it
    if name not in result_dict:
        result_dict[name] = []

    result_dict[name].append(value)

# Display the result with the original order of the 'Name' column
for name, values in result_dict.items():
    result = validate_and_concat(values)
    print(f"# {name}:\n{result}")


