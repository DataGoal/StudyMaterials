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


def get_schema_mapping(map):
    schema_map = [(key, val) for key, val in map.get("schema", {}).items()]
    return schema_map
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


def get_time_diff(start_time, end_time):
    start_timestamp = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    end_timestamp = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
    time_diff = end_timestamp - start_timestamp
    hours, mins, secs = map(int, str(time_diff).split(":"))
    time_different = f"{hours}h {mins}m {secs}s"
    return time_different


from datetime import datetime
from your_module import \
    get_time_diff  # Replace 'your_module' with the actual module name or file where the function is defined


def test_get_time_diff():
    start_time = '2022-01-01 12:00:00'
    end_time = '2022-01-01 14:30:45'
    expected_result = '2h 30m 45s'

    result = get_time_diff(start_time, end_time)

    assert result == expected_result


# Run the test
if __name__ == '__main__':
    test_load_yaml_content()
