import csv
with open("user_details.csv", newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    iterable_csv = iter(csv_reader)
    next(iterable_csv)

    for row in iterable_csv:
        print(row)
