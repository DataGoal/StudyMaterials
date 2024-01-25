import pytest

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
def test_get_value_by_key():
    # Test case 1: Key exists in the dictionary
    data_case1 = {'key1': 'value1', 'key2': 'value2'}
    target_key_case1 = 'key1'
    result_case1 = get_value_by_key(data_case1, target_key_case1)
    assert result_case1 == 'value1'

    # Test case 2: Key does not exist in the dictionary
    target_key_not_exist_case2 = 'key3'
    with pytest.raises(KeyError, match=f"The key {target_key_not_exist_case2} does not exist in the config file."):
        with pytest.raises(KeyError) as excinfo_case2:
            get_value_by_key(data_case1, target_key_not_exist_case2)
        assert str(excinfo_case2.value) == f"The key {target_key_not_exist_case2} does not exist in the config file."




def get_time_diff(start_time, end_time):
    """ Returns the time difference between end_time and start_time. """
    start_timestamp = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    end_timestamp = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')

    timestamp_diff = end_timestamp - start_timestamp
    hours, minutes, seconds = map(int, str(timestamp_diff).split(":"))
    time_diff = f"{hours}h {minutes}m {seconds}s"

    return time_diff


# Run the tests
if __name__ == '__main__':
    pytest.main([__file__])
