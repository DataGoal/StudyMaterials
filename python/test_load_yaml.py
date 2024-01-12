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
    # Test Case 1: Success case with the provided YAML content
    yaml_content = """
    unity_catalog:
      - catalog_name: main
        schemas:
          - schema_name: gold
            location: s3a://gold
          - schema_name: silver
            location: s3a://silver
      - catalog_name: stage
        schemas:
          - schema_name: gold
            location: s3a://gold
          - schema_name: silver
            location: s3a://silver

    ddl_creation:
      base_path: /file/path
      catalog_name: gold
      schemas:
        - tgt_schema: stage
          src_schema: "staging"
        - tgt_schema: pre_stage
          src_schema: "pre_staging"
        - tgt_schema: land
          src_schema: "landing"
    """

    with tempfile.NamedTemporaryFile(mode='w+', suffix='.yaml', delete=False) as temp_file:
        temp_file.write(yaml_content)
        temp_file_path = temp_file.name

    try:
        result = load_yaml_content(temp_file_path)
        expected_result = yaml.safe_load(yaml_content)
        print(expected_result)
        assert result == expected_result
    finally:
        os.remove(temp_file_path)




# Run the test
if __name__ == '__main__':
    test_load_yaml_content()
