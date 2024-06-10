import csv

def create_new_csv_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file, open(output_filename, 'w', encoding='utf-8', newline='') as output_file:
            reader = csv.reader(input_file)
            writer = csv.writer(output_file)
            for row in reader:
                # Replace any "\n" within the row and write the modified row to the output file
                cleaned_row = [cell.replace("\n", "") for cell in row]
                # Check if the row is not empty
                if any(cell.strip() for cell in cleaned_row):
                    writer.writerow(cleaned_row)
    except FileNotFoundError:
        print("File not found!")

# Call the function to create the new CSV file
create_new_csv_file("airbnb_NYC.csv", "newFile.csv")
