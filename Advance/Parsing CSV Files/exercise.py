import csv

# Open the input CSV file
with open('inputfile.csv', mode='r') as infile:
    reader = csv.reader(infile)
    # Open the output CSV file
    with open('outputfile.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        # Write header
        header = next(reader)
        writer.writerow(header)
        # Write rows where the value in the first column is greater than 50
        for row in reader:
            if int(row[0]) > 50:  # Assuming the first column contains numeric values
                writer.writerow(row)