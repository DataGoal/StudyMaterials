import pandas as pd

# Read the CSV file
df = pd.read_csv('C:\\Users\\bbala\\Desktop\\BBC\\GIT\\StudyMaterials\\inputs\\checking.csv', header=None, names=['Name', 'Value'])

# Group by 'Name' and aggregate 'Value' into a list
grouped_data = df.groupby('Name')['Value'].agg(list).reset_index()

# Create a function to validate and concatenate values
def validate_and_concat(values):
    return 'validate' + '_'.join(map(str, values))

# Apply the function to the 'Value' column
grouped_data['Result'] = grouped_data['Value'].apply(validate_and_concat)

# Display the result
print(grouped_data[['Name', 'Result']])
