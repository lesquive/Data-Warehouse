import csv
import os

def has_null_values(row):
    return any(value is None or value == '' for value in row)

def remove_rows_with_nulls(input_csv_path, output_csv_path):
    with open(input_csv_path, 'r', newline='', encoding='utf-8') as input_file:
        with open(output_csv_path, 'w', newline='', encoding='utf-8') as output_file:
            csv_reader = csv.reader(input_file)
            csv_writer = csv.writer(output_file)
            
            for row in csv_reader:
                if not has_null_values(row):
                    csv_writer.writerow(row)

def process_all_csv_files(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            input_csv_path = os.path.join(input_folder, filename)
            output_csv_path = os.path.join(output_folder, filename)
            remove_rows_with_nulls(input_csv_path, output_csv_path)

if __name__ == "__main__":
    input_folder = 'processed_csv'  # Replace with your input folder containing CSV files
    output_folder = 'no_nulls_csv'  # Replace with the desired output folder

    process_all_csv_files(input_folder, output_folder)
