import yaml
from pyspark.sql import SparkSession
from pyspark.sql.functions import length, row_number
from pyspark.sql.window import Window

def initialize_spark_session():
    return SparkSession.builder.appName("example").getOrCreate()

def read_table_as_dataframe(catalog_name, src_schema_name, src_table_name):
    return spark.read.table(f'{catalog_name}.{src_schema_name}.{src_table_name}')

def clone_columns_with_prefix(df, src_alias_name, prefix):
    columns_from_table = df.columns
    return [f'{prefix}{src_alias_name}.{column}' for column in columns_from_table]

def generate_row_number_column(df, src_alias_name, partition_col, order_cols):
    window_spec = Window.partitionBy(partition_col).orderBy(order_cols)
    return row_number().over(window_spec).alias("rec_num")

def generate_select_columns(df, src_alias_name, cloned_columns, length_columns, row_number_column):
    select_columns = ', '.join([
        f'{src_alias_name}.{column}, {cloned_column}, {length(src_alias_name}.{column}).alias("{length_column}")'
        for column, cloned_column, length_column in zip(df.columns, cloned_columns, length_columns)
    ])
    return f'{select_columns}, 1 as dummy_col, {row_number_column}'

def generate_join_clause(join_info, src_alias_name):
    join_type = join_info.get('join_type', 'LEFT OUTER')
    join_keys = join_info.get('join_keys', {})

    nvl_statement = f"NVL({join_info['ref_alias_name']}.{join_info['column_name']}, 'N') AS {join_info['flag_name']}"

    join_conditions = [
        f'{src_alias_name}.{src_key} = {join_info["ref_alias_name"]}.{ref_key}'
        for src_key, ref_key in join_keys.items()
    ]

    join_clause = (
        f'{join_type} JOIN {catalog_name}.{join_info["reference_schema_name"]}.{join_info["reference_table_name"]} {join_info["ref_alias_name"]} '
        f'ON {" AND ".join(join_conditions)}'
    )

    return nvl_statement, join_clause

def stop_spark_session():
    spark.stop()

def generate_sql_query(yaml_data):
    global spark, catalog_name

    catalog_name = yaml_data.get('catalog_name')
    src_schema_name = yaml_data.get('src_schema_name')
    src_table_name = yaml_data.get('src_table_name')
    src_alias_name = yaml_data.get('src_alias_name')

    flags = yaml_data.get('flags', [])

    spark = initialize_spark_session()
    df = read_table_as_dataframe(catalog_name, src_schema_name, src_table_name)

    cloned_columns = clone_columns_with_prefix(df, src_alias_name, 'ORIG_')
    length_columns = clone_columns_with_prefix(df, src_alias_name, 'LEN_')

    row_number_col = generate_row_number_column(df, src_alias_name, 1, ["INDEX", "ROW_OFFSET"])

    select_columns = generate_select_columns(df, src_alias_name, cloned_columns, length_columns, row_number_col)

    join_clauses = []
    nvl_statements = []

    for flag_info in flags:
        flag_name = next(iter(flag_info.keys()))
        join_info = flag_info[flag_name]

        nvl_statement, join_clause = generate_join_clause(join_info, src_alias_name)
        nvl_statements.append(nvl_statement)
        join_clauses.append(join_clause)

    stop_spark_session()

    sql_query = (
        f'SELECT {select_columns}\n'
        f'{",".join(nvl_statements)}\n'
        f'FROM {catalog_name}.{src_schema_name}.{src_table_name} {src_alias_name}\n'
        f'{"".join(join_clauses)};'
    )

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
sql_query = generate_sql_query(yaml_data)
print(sql_query)
