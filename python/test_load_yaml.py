import os
import tempfile
import yaml


def load_yaml_content(yaml_file_path):
    try:
        with open(yaml_file_path, 'r') as file:
            yaml_content = yaml.safe_load(file)
        return yaml_content
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        return None


def test_load_yaml_content():
    # Test Case 1: Success case with complex YAML content
    yaml_content = {
        'name': 'John Doe',
        'age': 30,
        'contacts': {
            'email': 'john.doe@example.com',
            'phone': '+123456789'
        },
        'addresses': [
            {'city': 'New York', 'zip_code': '10001'},
            {'city': 'Los Angeles', 'zip_code': '90001'}
        ]
    }

    with tempfile.NamedTemporaryFile(mode='w+', suffix='.yaml', delete=False) as temp_file:
        yaml.dump(yaml_content, temp_file)
        temp_file_path = temp_file.name

    try:
        result = load_yaml_content(temp_file_path)
        assert result == yaml_content
    finally:
        os.remove(temp_file_path)

    # Test Case 2: Failure case with non-YAML content
    with tempfile.NamedTemporaryFile(mode='w+', suffix='.txt', delete=False) as temp_file:
        temp_file_path = temp_file.name

    try:
        result = load_yaml_content(temp_file_path)
        assert result is None
    finally:
        os.remove(temp_file_path)


# Run the test
if __name__ == '__main__':
    test_load_yaml_content()
