import re


def new_schema(catalog_name, schema_name, s3_path, spark):
    try:
        spark.sql(f"""CREATE SCHEMA IF NOT EXISTS {catalog_name}.{schema_name} MANAGED LOCATION {s3_path};""")
        print(f"Schema created successfully")
    except Exception as e:
        raise RuntimeError(f"Error occurred while creating new schema")

original_string = "CLOB(16384) LOGGED NOT COMPACT"
replacement_string = "STRING"

# Use a regular expression to match the pattern "CLOB(?*)" where "?" can be any number
pattern = re.compile(r'CLOB\(\d+\) LOGGED NOT COMPACT')

# Replace the matched pattern with the replacement string
new_string = re.sub(pattern, replacement_string, original_string)

print(new_string)
