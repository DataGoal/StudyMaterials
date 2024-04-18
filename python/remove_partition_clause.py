def remove_partition_clause(sql_query):
    # Find the index of 'partition by' in the query (case-insensitive)
    index_partition_by = sql_query.lower().find('partition by')

    if index_partition_by != -1:
        # Find the start and end indices of the 'partition by' clause
        start_index = index_partition_by
        end_index = sql_query.find(')', start_index) + 1  # Find the end of the partition clause

        # Remove the 'partition by' clause from the original query
        modified_query = sql_query[:start_index] + sql_query[end_index:]

        return modified_query.strip()
    else:
        # Return the original query if 'partition by' is not found
        return sql_query.strip()


# Example usage
original_query = """
CREATE TABLE employee
(
name string,
id int,
age int,
address string
)
partition by(id)
TBLPROPERTIES(
'delta' = 'true',
'version'='1');
"""

# Remove the 'partition by' clause from the original query
modified_query = remove_partition_clause(original_query)
print(modified_query)
