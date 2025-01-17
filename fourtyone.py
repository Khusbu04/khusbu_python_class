import csv
file_path = "reads_data.csv"
def create_sd():
    headers = ["category", "Value1", "Value2", "Value3"]
    with open(file_path, mode = "w", newlines = "") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
    print("CSV file created.")
def add_data(category, value1, value2, value3)
    with open(file_csv, mode = "a", newline = "'") as file:
        writer = csv.writer(file)
        writer.writerow([n])

    
