import sys
import csv
from tabulate import tabulate
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

try:
    with open(sys.argv[1],"r") as file:
        reader = csv.reader(file)
        table = tabulate(reader,tablefmt="outline",headers="firstrow")
        print(table)
except FileNotFoundError:
    if sys.argv[1].endswith(".csv"):
        sys.exit("file does not exists")
    else:
        sys.exit("file is not a csv")

