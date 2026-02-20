import sys
import csv

if len(sys.argv) != 3:
    sys.exit("Usage: python scourgify.py input.csv output.csv")

try:
    with open(sys.argv[1], "r", newline="") as infile, \
         open(sys.argv[2], "w", newline="") as outfile:

        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])

        writer.writeheader()

        for row in reader:
            last, first = row["name"].split(",")
            writer.writerow({
                "first": first.strip(),
                "last": last.strip(),
                "house": row["house"]
            })

except FileNotFoundError:
    sys.exit("Input file does not exist")