import csv
def parse_csv_for_totals(file_path):
    # Initialize containers for row and column totals
    row_totals = {}
    column_totals = {}
    with open(file_path, mode = "r") as file:
        reader = csv.reader(file)
        headers = next(reader) # Read the header rrow
        # InItalize column totals dictionary with column names
        for header in headers[1:]:
            column_totals[header]=0


             # Skio he first column(Category)
        # Process rows
        for row in reader:
            category = row[0] # First column is the category
            #category = A
            values = list(map(int, row[1:])) # Convert the rest of the row to 
            # values = [10, 20, 30]
            # calculate row total
            row_totals[category] = sum(values)
            #Update column totals
            for header, value in zip(headers[1:], values):
                column_totals[header] += value
    # output results
    print("Row Total:")
    for category, total in row_totals.items():
        print(f"{category}: {total}")
    print("\nColumn Totals:")
    for column, total in column_totals.items():
        print(f"{column}: {total}")
# Example Usage
file_path = "parser_data.csv"
parse_csv_for_totals(file_path)