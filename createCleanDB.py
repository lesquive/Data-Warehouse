import pyodbc
import os
import csv

# Set up the connection parameters for the new database
new_db_server ='LAPTOP-6MKQR2UG\SQLEXPRESS'
new_db_name = 'ProyectoGrupo2Clean'
new_db_connection_string = f"Driver={{SQL Server}};Server={new_db_server};Database={new_db_name};Trusted_Connection=yes;"

def create_table(cursor, table_name, column_names):
    columns = ', '.join(f'{name} NVARCHAR(MAX)' for name in column_names)
    create_table_query = f"CREATE TABLE {table_name} ({columns})"
    cursor.execute(create_table_query)
    
def insert_row(cursor, table_name, values):
    placeholders = ', '.join('?' for _ in values)
    insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
    cursor.execute(insert_query, values)

def process_csv_file(file_path, cursor, table_name):
    with open(file_path, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        create_table(cursor, table_name, header)

        for row in csv_reader:
            insert_row(cursor, table_name, row)

if __name__ == "__main__":
    no_nulls_csv_folder = 'no_nulls_csv'  # Replace with the path to your no_nulls_csv folder

    try:
        # Establish the connection to the new database
        new_db_conn = pyodbc.connect(new_db_connection_string)
        new_db_cursor = new_db_conn.cursor()

        for filename in os.listdir(no_nulls_csv_folder):
            if filename.endswith(".csv"):
                table_name = os.path.splitext(filename)[0]
                file_path = os.path.join(no_nulls_csv_folder, filename)
                process_csv_file(file_path, new_db_cursor, table_name)
                new_db_conn.commit()

    except pyodbc.Error as e:
        print("Error:", e)

    finally:
        # Close the cursor and connection
        new_db_cursor.close()
        new_db_conn.close()
