from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.types import StringType, BooleanType, StructField, StructType


def compare_fields_pyspark(val1, val2):
    # Initialize Spark session
    spark = SparkSession.builder.appName("FieldComparison").getOrCreate()

    # Convert input lists to dictionaries for easy lookup
    dict1 = {item[0]: item[1] for item in val1}
    dict2 = {item[0]: item[1] for item in val2}

    # Find all unique field names from both dictionaries
    all_fields = set(dict1.keys()).union(set(dict2.keys()))

    # Prepare the comparison list
    comparison = []
    for field in all_fields:
        df1_field_name = field if field in dict1 else 'NA'
        df1_datatype = dict1[field].__name__ if field in dict1 else 'NA'
        df2_field_name = field if field in dict2 else 'NA'
        df2_datatype = dict2[field].__name__ if field in dict2 else 'NA'
        field_cmp = df1_field_name == df2_field_name
        datatype_cmp = df1_datatype == df2_datatype
        comparison.append((df1_field_name, df1_datatype, df2_field_name, df2_datatype, field_cmp, datatype_cmp))

    # Convert comparison list to Row objects
    rows = [
        Row(df1_field_name=row[0], df1_datatype=row[1], df2_field_name=row[2], df2_datatype=row[3], field_cmp=row[4],
            datatype_cmp=row[5]) for row in comparison]

    # Define the schema for the PySpark DataFrame
    schema = StructType([
        StructField("df1_field_name", StringType(), True),
        StructField("df1_datatype", StringType(), True),
        StructField("df2_field_name", StringType(), True),
        StructField("df2_datatype", StringType(), True),
        StructField("field_cmp", BooleanType(), True),
        StructField("datatype_cmp", BooleanType(), True)
    ])

    # Create a Spark DataFrame
    df = spark.createDataFrame(rows, schema)

    return df


# Example usage
val1 = [('emp_name', str), ('emp_id', int), ('emp_adrs', str)]
val2 = [('emp_name', str), ('emp_id', str), ('cus_name', str)]

df = compare_fields_pyspark(val1, val2)
df.show()
