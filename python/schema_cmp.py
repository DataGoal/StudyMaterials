from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, col


def compare_schemas(val1, val2):
    # Initialize Spark session
    spark = SparkSession.builder.master("local").appName("Schema Comparison").getOrCreate()

    # Create DataFrames from input lists
    df1 = spark.createDataFrame(val1, ["field_name", "data_type"])
    df2 = spark.createDataFrame(val2, ["field_name", "data_type"])

    # Perform a full outer join on field_name
    joined_df = df1.join(df2, df1.field_name == df2.field_name, "full_outer") \
        .select(df1["field_name"].alias("df1_field_name"), df1["data_type"].alias("df1_datatype"),
                df2["field_name"].alias("df2_field_name"), df2["data_type"].alias("df2_datatype"))

    # Fill NA values for missing fields in the join
    joined_df = joined_df.fillna("NA", subset=["df1_field_name", "df2_field_name", "df1_datatype", "df2_datatype"])

    # Add comparison columns
    joined_df = joined_df.withColumn("field_cmp", (col("df1_field_name") == col("df2_field_name"))) \
        .withColumn("datatype_cmp", (col("df1_datatype") == col("df2_datatype")))

    # Show the result
    joined_df.show(truncate=False)

    return joined_df


# Define the input lists
val1 = [('emp_name', 'string'), ('emp_id', 'int'), ('emp_adrs', 'string')]
val2 = [('emp_name', 'string'), ('emp_id', 'string'), ('cus_name', 'string')]

# Call the function with the input lists
compare_schemas(val1, val2)
