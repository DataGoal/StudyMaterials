from pyspark.sql import SparkSession
from pyspark.sql.functions import lit


def compare_schemas(val1, val2):
    # Initialize Spark session
    spark = SparkSession.builder.master("local").appName("Schema Comparison").getOrCreate()

    # Convert the input lists to DataFrames
    df1 = spark.createDataFrame(val1, ["field_name", "data_type"])
    df2 = spark.createDataFrame(val2, ["field_name", "data_type"])

    # Add a source column to distinguish between the two DataFrames
    df1 = df1.withColumn("source", lit("df1"))
    df2 = df2.withColumn("source", lit("df2"))

    # Perform a full outer join on the field_name column
    joined_df = df1.join(df2, df1.field_name == df2.field_name, "full_outer") \
        .select(df1["field_name"].alias("df1_field_name"), df1["data_type"].alias("df1_datatype"),
                df2["field_name"].alias("df2_field_name"), df2["data_type"].alias("df2_datatype"))

    # Fill NA values for missing fields in the join
    joined_df = joined_df.fillna("NA")

    # Add comparison columns
    joined_df = joined_df.withColumn("field_cmp", (joined_df["df1_field_name"] == joined_df["df2_field_name"])) \
        .withColumn("datatype_cmp", (joined_df["df1_datatype"] == joined_df["df2_datatype"]))

    # Show the result
    joined_df.show()

    return joined_df


# Define the input lists
val1 = [('emp_name', 'string'), ('emp_id', 'int'), ('emp_adrs', 'string')]
val2 = [('emp_name', 'string'), ('emp_id', 'string'), ('cus_name', 'string')]

# Call the function with the input lists
compare_schemas(val1, val2)
