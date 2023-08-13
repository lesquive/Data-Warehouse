import pyodbc
import csv
import os

# Set up the connection parameters
server = 'LAPTOP-6MKQR2UG\SQLEXPRESS'
database = 'ProyectoGrupo2'
connection_string = f"Driver={{SQL Server}};Server={server};Database={database};Trusted_Connection=yes;"

# Output directory for CSV files
output_directory = 'DB-a-csv'
os.makedirs(output_directory, exist_ok=True)

try:
    # Establish the connection
    conn = pyodbc.connect(connection_string)

    # Create a cursor to interact with the database
    cursor = conn.cursor()

    # Get the list of tables in the database
    tables_query = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'"
    tables = [row[0] for row in cursor.execute(tables_query).fetchall()]

    # Iterate through tables and write data to CSV files
    for table in tables:
        select_query = f"SELECT * FROM {table}"
        cursor.execute(select_query)
        columns = [column[0] for column in cursor.description]

        csv_file_path = os.path.join(output_directory, f"{table}.csv")
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(columns)
            for row in cursor.fetchall():
                csv_writer.writerow(row)

except pyodbc.Error as e:
    print("Error:", e)

finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()
