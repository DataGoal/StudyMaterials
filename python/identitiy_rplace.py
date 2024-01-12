import re

def replace_identity(input_str):
    # Define the pattern for matching "identity (...)"
    pattern = re.compile(r'identity\s*\([^)]*\)')

    # Replace the matched pattern with 'bala'
    output_str = re.sub(pattern, 'bala', input_str)

    return output_str

# Test the function with your input
input_str = 'CREATE table tab_name (alaway as identity (SAR, ASDV, asd), col1)'
output_str = replace_identity(input_str)

print(output_str)
