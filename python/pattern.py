def extract_text_between_brackets(input_string):
    open_bracket_index = input_string.find('(')

    if open_bracket_index != -1:
        close_bracket_index = input_string.find(')', open_bracket_index)

        if close_bracket_index != -1:
            extracted_text = input_string[open_bracket_index:close_bracket_index + 1]
            return extracted_text

    return None


# Example usage
input_string = 'My name is (Bob, and my age is (10), living in (Marsh)) and whats up'
result = extract_text_between_brackets(input_string)

if result:
    print(result)
else:
    print("No matching brackets found.")
