import yaml

# Load YAML file
with open('C:\\Users\\bbala\\Desktop\\BBC\\GIT\\StudyMaterials\\inputs\\config.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Function to generate SQL statements
def generate_sql(catalog):
    sql_statements = []
    for entry in catalog:
        # entry is the catalog name, not a dictionary
        catalog_name = entry
        sql_statements.append(f'USE CATALOG {catalog_name};')
        for schema in catalog[entry]:
            schema_name = schema['schema_name']
            location = schema['location']
            sql_statements.append(f'CREATE SCHEMA {schema_name} LOCATION {location};')
    return sql_statements

# Generate and print SQL statements
for catalog in data['unity_catalog']:
    catalog_name = catalog.get('catalog_name')
    schemas = catalog.get('schemas')

    for schema in schemas:
        schema_name = schema.get('schema_name', '')
        location = schema.get('location')
        print(f'{catalog_name}.{schema_name}.{location}')

import yaml

# Your provided YAML data
yaml_data = """
ddl_creation:
  base_path: /file/path
  catalog_name: gold
  schemas:
    - tgt_schema: stage
      src_schema: "staging  "
    - tgt_schema: pre_stage
      src_schema: "pre_staging"
    - tgt_schema: land
      src_schema: "landing"
"""

# Load YAML data
data = yaml.safe_load(yaml_data)

# Extract relevant information and build the dictionary
ddl_dict = {schema['tgt_schema']: schema['src_schema'].strip() for schema in data['ddl_creation']['schemas']}

# Print the resulting dictionary
print(ddl_dict)

ddl_dict = {'stage': 'staging', 'pre_stage': 'pre_staging', 'land': 'landing'}

for key, value in ddl_dict.items():
    print(f"{key}: {value}")


