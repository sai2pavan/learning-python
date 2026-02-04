import sys
if len(sys.argv) < 2:
    sys.exit("Too Frew Arguments")

for arg in sys.argv[1:-1]:
    print("Hello, my name is",arg)