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


def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content


def get_value_by_key(data, target_key):
    """ Returns the value for the given key; raises KeyError if the key does not exist. """
    try:
        value = data.get(target_key)
        if value is not None:
            return value
        else:
            raise KeyError(f"The key {target_key} does not exists in the config file.")
    except Exception as e:
        raise Exception(f"An error occurred while retrieving the key from config file.")


def ship_variables_to_yaml(yaml_content, variables):
    """ Renders the dict map values into it's yaml key variables. """
    template = Template(yaml_content)
    return template.render(variables)


def get_parametrized_yaml(unity_catalog_config, accounts_config, env):
    """ Gets the raw YAML's and returns parsed YAML with the substituted key variables."""
    catalog_config = read_file(unity_catalog_config)
    account_number = read_account_details(accounts_config, env)
    env_variables = {"env": env, "account_number": account_number}
    parsed_yaml = ship_variables_to_yaml(catalog_config, env_variables)
    yaml_content = yaml.safe_load(parsed_yaml)
    return yaml_content


def test_get_value_by_key():
    # Test case 1: Key exists in the dictionary
    data = {'key1': 'value1', 'key2': 'value2'}
    target_key = 'key1'
    result = get_value_by_key(data, target_key)
    assert result == 'value1'

    # Test case 2: Key does not exist in the dictionary
    target_key_not_exist = 'key3'
    with pytest.raises(KeyError, match=f"The key {target_key_not_exist} does not exist in the config file."):
        get_value_by_key(data, target_key_not_exist)

    # Test case 3: Error handling
    data_with_error = {'key1': 'value1', 'key2': 'value2'}
    target_key_with_error = 'key3'
    with pytest.raises(Exception, match="An error occurred while retrieving the key from config file."):
        get_value_by_key(data_with_error, target_key_with_error)


def test_ship_variables_to_yaml():
    # Test case 1: Valid YAML content and variables
    yaml_content_case1 = "name: {{ name }}, age: {{ age }}"
    variables_case1 = {'name': 'John', 'age': 30}
    expected_result_case1 = "name: John, age: 30"
    result_case1 = ship_variables_to_yaml(yaml_content_case1, variables_case1)
    assert result_case1 == expected_result_case1

    # Test case 2: Valid YAML content but empty variables
    yaml_content_case2 = "name: {{ name }}, age: {{ age }}"
    variables_case2 = {}
    expected_result_case2 = "name: , age: "
    result_case2 = ship_variables_to_yaml(yaml_content_case2, variables_case2)
    assert result_case2 == expected_result_case2

    # Test case 3: Empty YAML content and variables
    yaml_content_case3 = ""
    variables_case3 = {'name': 'John', 'age': 30}
    expected_result_case3 = ""
    result_case3 = ship_variables_to_yaml(yaml_content_case3, variables_case3)
    assert result_case3 == expected_result_case3


def test_get_parametrized_yaml(tmpdir):
    # Create temporary files for testing
    unity_catalog_config = tmpdir.join("unity_catalog_config.yaml")
    accounts_config = tmpdir.join("accounts_config.yaml")

    # Write content to temporary files
    unity_catalog_content = "catalog_key: {{ env }}, account_key: {{ account_number }}"
    accounts_content = "account_number: 123456"
    unity_catalog_config.write(unity_catalog_content)
    accounts_config.write(accounts_content)

    # Test the get_parametrized_yaml function
    env = "test_env"
    result = get_parametrized_yaml(str(unity_catalog_config), str(accounts_config), env)

    # Define the expected result after substitution
    expected_result = {'catalog_key': 'test_env', 'account_key': '123456'}

    # Assert that the result matches the expected result
    assert result == expected_result

