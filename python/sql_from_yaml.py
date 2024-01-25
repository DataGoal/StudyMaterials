import yaml


def generate_sql_from_yaml(yaml_data):
    catalog_name = yaml_data.get('catalog_name')
    src_schema_name = yaml_data.get('src_schema_name')
    src_table_name = yaml_data.get('src_table_name')
    src_alias_name = yaml_data.get('src_alias_name')

    flags = yaml_data.get('flags', [])

    select_columns = f'{src_alias_name}.*,'

    join_clauses = []
    case_statements = []

    for flag_info in flags:
        flag_name = next(iter(flag_info.keys()))
        join_info = flag_info[flag_name]

        join_type = join_info.get('join_type', 'LEFT OUTER')
        join_keys = join_info.get('join_keys', {})

        case_statement = f'CASE WHEN {join_info["ref_alias_name"]}.{join_info["column_name"]} IS NOT NULL THEN \'Y\' ELSE \'N\' END AS {join_info["flag_name"]}'
        case_statements.append(case_statement)

        join_conditions = []
        for src_key, ref_key in join_keys.items():
            join_conditions.append(f'{src_alias_name}.{src_key} = {join_info["ref_alias_name"]}.{ref_key}')

        join_clause = f'{join_type} JOIN {catalog_name}.{join_info["reference_schema_name"]}.{join_info["reference_table_name"]} {join_info["ref_alias_name"]} ON {" AND ".join(join_conditions)}'
        join_clauses.append(join_clause)

    sql_query = f'SELECT {select_columns}\n' \
                f'{",".join(case_statements)}\n' \
                f'FROM {catalog_name}.{src_schema_name}.{src_table_name} {src_alias_name}\n' \
                f'{"".join(join_clauses)};'

    return sql_query


# Example usage
yaml_data = """
catalog_name: db
src_schema_name: gold
src_table_name: emp_table
src_alias_name: alias_emp_table
flags:
  - cntry_flag:
      flag_name: COUNTRY_EXIST_FLAG
      reference_schema_name: silver
      reference_table_name: sal_table
      ref_alias_name: alias_sal_table
      column_name: COUNTRY_CODE
      join_type: left outer
      join_keys:
        foo: bar
        dog: cat
  - state_flag:
      flag_name: STATE_EXIST_FLAG
      reference_schema_name: silver
      reference_table_name: rav_table
      ref_alias_name: alias_rav_table
      column_name: STATE_CODE
      join_type: left outer
      join_keys:
        food: bond
        gan: nag
"""

yaml_data = yaml.safe_load(yaml_data)
sql_query = generate_sql_from_yaml(yaml_data)
print(sql_query)
