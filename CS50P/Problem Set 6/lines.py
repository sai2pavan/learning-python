import sys
if len(sys.argv) > 2:
    sys.exit("too many arguments")
elif len(sys.argv) < 2:
    sys.exit("too few arguments")

try:
    count = 0
    with open(sys.argv[1],"r") as file:
        for line in file:
            stripped = line.lstrip()

            if stripped == "":
                continue
            if stripped.startswith("#"):
                continue
            count += 1
except FileNotFoundError:
    sys.exit("File does not exists")

print(count)