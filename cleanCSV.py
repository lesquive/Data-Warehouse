import csv
import re
import os

def remove_accents(raw_text):
    """Removes common accent characters."""
    print("Raw Text:", raw_text)  # Print the raw text before processing
    if "DÃ­a de spa" in raw_text:
        raw_text = raw_text.replace("DÃ­a de spa", "Dia de spa")
    if "vehÃ­culo" in raw_text:
        raw_text = raw_text.replace("vehÃ­culo", "vehiculo")
    if "de juegos" in raw_text:
        raw_text = raw_text.replace(raw_text, "Area de juegos")
    raw_text = re.sub(u"Ã±", 'n', raw_text)
    raw_text = re.sub(u"Ã©", 'e', raw_text)
    raw_text = re.sub(u"Ã³", 'o', raw_text)
    raw_text = re.sub(u"Ãº", 'u', raw_text)
    raw_text = re.sub(u"Ã¡", 'a', raw_text)
    raw_text = re.sub(u"ñ", 'n', raw_text)
    return raw_text

def process_csv(input_csv_path, output_csv_path):
    with open(input_csv_path, 'r', newline='', encoding='utf-8') as input_file:
        with open(output_csv_path, 'w', newline='', encoding='utf-8') as output_file:
            csv_reader = csv.reader(input_file)
            csv_writer = csv.writer(output_file)
            
            for row in csv_reader:
                processed_row = [remove_accents(value) if isinstance(value, str) else value for value in row]
                csv_writer.writerow(processed_row)

def process_all_csv_files(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            input_csv_path = os.path.join(input_folder, filename)
            output_csv_path = os.path.join(output_folder, filename)
            process_csv(input_csv_path, output_csv_path)

if __name__ == "__main__":
    input_folder = 'output_csv'  # Replace with your input folder containing CSV files
    output_folder = 'processed_csv'  # Replace with the desired output folder

    process_all_csv_files(input_folder, output_folder)
