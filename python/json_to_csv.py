import json
import csv


# Function to read JSON file and convert to CSV
def json_to_csv(json_file, csv_file):
    # Load JSON data from file
    with open(json_file, 'r') as f:
        json_data = json.load(f)

    # Extract relevant data
    tables = json_data["Tables"]

    # Open CSV file for writing
    with open(csv_file, 'w', newline='') as f:
        csv_writer = csv.writer(f)

        # Write header row
        header = ["Schema", "TableNames", "PartitionColumn"]
        csv_writer.writerow(header)

        # Write data rows
        for table in tables:
            schema = table["Schema"]
            for table_name in table["TableNames"]:
                partition_column = table["PartitionColumn"]
                csv_writer.writerow([schema, table_name, partition_column])


# Specify the JSON and CSV file paths
json_file_path = 'data.json'  # Replace with your JSON file path
csv_file_path = 'output.csv'  # Desired CSV output file path

# Convert JSON to CSV
json_to_csv(json_file_path, csv_file_path)

print(f"JSON data has been written to {csv_file_path}")

from pyspark.sql import SparkSession
from pyspark.sql.functions import split, when, col

# Initialize SparkSession
spark = SparkSession.builder.appName("SplitEventColumn").getOrCreate()

# Sample data with and without '='
data = [("date=0102",), ("date=0103",), ("date=0104",), ("0105",), ("0106",)]
columns = ["event"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Split the 'event' column by '=' and handle cases without '='
df = df.withColumn(
    "event",
    when(col("event").contains("="), split(col("event"), "=").getItem(1)).otherwise(col("event"))
)

# Show the resulting DataFrame
df.show()
