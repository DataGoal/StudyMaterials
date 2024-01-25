from pyspark.sql.types import StructType, StructField, StringType


def df_from_parquet(file_path, spark):
    """ Reads a Parquet file and returns a Dataframe. """
    return spark.read.parquet(file_path)


def save_delta_table_with_partitions(df, catalog_name, schema_name, table_name, partition_cols,
                                     write_mode="overwrite"):
    """ Saves a Dataframe into a delta table with the partition columns. """
    df.write.format("delta").mode(write_mode).partitionBy(partition_cols.split(",")).option("overwriteSchema",
                                                                                            "true").saveAsTable(
        f"`{catalog_name}`.`{schema_name}`.`{table_name}`")


def save_parquet_data_with_partition(file_path, catalog_name, schema_name, table_name, partition_cols, spark,
                                     write_mode="overwrite"):
    """ Creates a dataframe from parquet file and saves into a delta table with partition columns. """
    df = df_from_parquet(file_path, spark)
    save_delta_table_with_partitions(df, catalog_name, schema_name, table_name, partition_cols, write_mode)


def test_save_parquet_data_with_partition(tmp_dbfs_dir, tmp_dbfs_catalog, tmp_dbfs_schema, spark):
    actual_table_name = "actual_table_1"
    expected_table_name = "expected_table_1"
    test_file_path = f"{tmp_dbfs_dir}/ccxcxample_parquet_file"
    write_mode = "overwrite"
    partition_cols = "foo, bar"
    schema = StructType([
        StructField("foo", StringType(), True),
        StructField("bar", StringType(), True),
        StructField("cat", StringType(), True)
    ])
    data = [
        {'foo': 'tom', 'bar': 'yam', 'cat': 'dog'},
        {'foo': 'rio', 'bar': 'mat', 'cat': 'tan'}
    ]
    df = spark.createDataFrame(data, schema=schema)

    df.write.parquet(test_file_path)

    parquet_df = spark.read.schema(schema).parquet(test_file_path)
    parquet_df.show(10, False)

    parquet_df.write.format("delta").mode(write_mode).partitionBy(partition_cols.split(",")).option("overwriteSchema",
                                                                                                    "true").saveAsTable(
        f"`{tmp_dbfs_catalog}`.`{tmp_dbfs_schema}`.`{actual_table_name}`")
    actual_partitions_df = spark.sql(
        f"""SHOW PARTITIONS `{tmp_dbfs_catalog}`.`{tmp_dbfs_schema}`.`{actual_table_name}`;""")

    save_parquet_data_with_partition(tmp_dbfs_dir, tmp_dbfs_catalog, tmp_dbfs_schema, expected_table_name,
                                     partition_cols, spark, write_mode)
    expected_partitions_df = spark.sql(
        f"""SHOW PARTITIONS `{tmp_dbfs_catalog}`.`{tmp_dbfs_schema}`.`{expected_table_name}`;""")

    assert sorted(expected_partitions_df.collect()) == sorted(actual_partitions_df.collect())


def load_parquet_data(ant_file_path, non_ant_file_path, catalog_name, databricks_schema, datastage_schema,
                      unity_catalog_config, accounts_config, env, spark):
    """ Reads the parquet file from a given file path and then loads into a delta table, parallely insert & update load
    status into a metadata table."""
    files_list = get_file_details(ant_file_path, non_ant_file_path, spark)
    table_partitions_map = get_table_prop_map_from_yaml(unity_catalog_config, accounts_config, "partition_columns", env)
    filter_conditions_map = get_table_prop_map_from_yaml(unity_catalog_config, accounts_config, "filter_conditions",
                                                         env)
    business_keys_map = get_table_prop_map_from_yaml(unity_catalog_config, accounts_config, "business_keys", env)
    create_adm_table(catalog_name, spark)

    try:
        for file in files_list:
            file_location = str(file[0])
            table_name = str(file[1].split("/")[0])
            databricks_table_name = f"{catalog_name}.{databricks_schema}.{table_name}"

            if databricks_table_name in table_partitions_map:
                partition_cols = table_partitions_map[databricks_table_name]
                start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                insert_adm_table(catalog_name, databricks_schema, datastage_schema, table_name, partition_cols,
                                 table_name, file_location, start_time, spark)
                setup_code = """
from src.spark.helpers.load_files_util import save_parquet_data_with_partition"""
                timing_code = """save_parquet_data_with_partition(file_location, catalog_name, databricks_schema, 
                table_name, filter_conditions_map, business_keys_map, partition_cols, spark)"""
                time_taken = timeit.timeit(stmt=timing_code, setup=setup_code,
                                           globals={'file_location': file_location, 'catalog_name': catalog_name,
                                                    'databricks_schema': databricks_schema, 'table_name': table_name,
                                                    'filter_conditions_map': filter_conditions_map,
                                                    'business_keys_map': business_keys_map,
                                                    'partition_cols': partition_cols, 'spark': spark}, number=1)
                end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                time_diff = "{:.2f}s".format(time_taken)
                row_count = get_row_count(catalog_name, databricks_schema, table_name, spark)
                update_adm_table(catalog_name, databricks_schema, table_name, start_time, end_time, time_diff,
                                 row_count, spark)
                print(f"Successfully loaded table {catalog_name}.{databricks_schema}.{table_name} with partition "
                      f"columns {partition_cols} from file path {file_location}")
            else:
                start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                insert_adm_table(catalog_name, databricks_schema, datastage_schema, table_name, "null",
                                 table_name, file_location, start_time, spark)
                setup_code = """
from src.spark.helpers.load_files_util import save_parquet_data_with_partition"""
                timing_code = """save_parquet_data_without_partition(file_location, catalog_name, databricks_schema, 
                table_name, filter_conditions_map, business_keys_map, spark)"""
                time_taken = timeit.timeit(stmt=timing_code, setup=setup_code,
                                           globals={'file_location': file_location, 'catalog_name': catalog_name,
                                                    'databricks_schema': databricks_schema, 'table_name': table_name,
                                                    'filter_conditions_map': filter_conditions_map,
                                                    'business_keys_map': business_keys_map,
                                                    'spark': spark}, number=1)
                end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                time_diff = "{:.2f}s".format(time_taken)
                row_count = get_row_count(catalog_name, databricks_schema, table_name, spark)
                update_adm_table(catalog_name, databricks_schema, table_name, start_time, end_time, time_diff,
                                 row_count, spark)
                print(
                    f"Successfully loaded table {catalog_name}.{databricks_schema}.{table_name} from file path {file_location}")
    except Exception as e:
        print(f"Error occurred while loading the file into table: {e} ")


import timeit
from datetime import datetime
from src.spark.helpers.load_files_util import save_parquet_data_with_partition, save_parquet_data_without_partition


def load_parquet_data(file_location, catalog_name, databricks_schema, datastage_schema, unity_catalog_config,
                      accounts_config, env, spark):
    """ Reads the parquet file from a given file path and then loads into a delta table, parallely insert & update load
    status into a metadata table."""
    files_list = get_file_details(file_location, spark)
    table_partitions_map = get_table_prop_map_from_yaml(unity_catalog_config, accounts_config, "partition_columns", env)
    filter_conditions_map = get_table_prop_map_from_yaml(unity_catalog_config, accounts_config, "filter_conditions",
                                                         env)
    business_keys_map = get_table_prop_map_from_yaml(unity_catalog_config, accounts_config, "business_keys", env)
    create_adm_table(catalog_name, spark)

    try:
        for file in files_list:
            file_location = str(file[0])
            table_name = str(file[1].split("/")[0])
            databricks_table_name = f"{catalog_name}.{databricks_schema}.{table_name}"

            if databricks_table_name in table_partitions_map:
                partition_cols = table_partitions_map[databricks_table_name]
                start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                insert_adm_table(catalog_name, databricks_schema, datastage_schema, table_name, partition_cols,
                                 table_name, file_location, start_time, spark)
                time_taken = process_with_partition(file_location, catalog_name, databricks_schema, table_name,
                                                    filter_conditions_map, business_keys_map, partition_cols, spark)
            else:
                start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                insert_adm_table(catalog_name, databricks_schema, datastage_schema, table_name, "null",
                                 table_name, file_location, start_time, spark)
                time_taken = process_without_partition(file_location, catalog_name, databricks_schema, table_name,
                                                       filter_conditions_map, business_keys_map, spark)

            end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            time_diff = "{:.2f}s".format(time_taken)
            row_count = get_row_count(catalog_name, databricks_schema, table_name, spark)
            update_adm_table(catalog_name, databricks_schema, table_name, start_time, end_time, time_diff,
                             row_count, spark)

            print(f"Successfully loaded table {catalog_name}.{databricks_schema}.{table_name} "
                  f"from file path {file_location}")

    except Exception as e:
        print(f"Error occurred while loading the file into table: {e} ")


def process_with_partition(file_location, catalog_name, databricks_schema, table_name, filter_conditions_map,
                           business_keys_map, partition_cols, spark):
    setup_code = """from src.spark.helpers.load_files_util import save_parquet_data_with_partition"""
    timing_code = """save_parquet_data_with_partition(file_location, catalog_name, databricks_schema, 
                    table_name, filter_conditions_map, business_keys_map, partition_cols, spark)"""
    return timeit.timeit(stmt=timing_code, setup=setup_code,
                         globals={'file_location': file_location,
                                  'catalog_name': catalog_name,
                                  'databricks_schema': databricks_schema,
                                  'table_name': table_name,
                                  'filter_conditions_map': filter_conditions_map,
                                  'business_keys_map': business_keys_map,
                                  'partition_cols': partition_cols,
                                  'spark': spark}, number=1)


def process_without_partition(file_location, catalog_name, databricks_schema, table_name, filter_conditions_map,
                              business_keys_map, spark):
    setup_code = """from src.spark.helpers.load_files_util import save_parquet_data_without_partition"""
    timing_code = """save_parquet_data_without_partition(file_location, catalog_name, databricks_schema, 
                    table_name, filter_conditions_map, business_keys_map, spark)"""
    return timeit.timeit(stmt=timing_code, setup=setup_code,
                         globals={'file_location': file_location,
                                  'catalog_name': catalog_name,
                                  'databricks_schema': databricks_schema,
                                  'table_name': table_name,
                                  'filter_conditions_map': filter_conditions_map,
                                  'business_keys_map': business_keys_map,
                                  'spark': spark}, number=1)
