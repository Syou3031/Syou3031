import csv
with open('file.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    print(header)
