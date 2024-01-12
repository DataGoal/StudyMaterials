import unittest
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

class TestLoadYamlContent(unittest.TestCase):

    def test_load_yaml_content(self):
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
            self.assertEqual(result, yaml_content)
        finally:
            os.remove(temp_file_path)

        # Test Case 2: Failure case with non-YAML content
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.txt', delete=False) as temp_file:
            temp_file_path = temp_file.name

        try:
            result = load_yaml_content(temp_file_path)
            self.assertIsNone(result)
        finally:
            os.remove(temp_file_path)

if __name__ == '__main__':
    unittest.main()