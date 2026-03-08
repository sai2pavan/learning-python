import sys
from PIL import Image, ImageOps


def main():

    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input output")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    valid_ext = [".jpg", ".jpeg", ".png"]

    input_ext = input_file.lower().split(".")[-1]
    output_ext = output_file.lower().split(".")[-1]

    if f".{input_ext}" not in valid_ext:
        sys.exit("Invalid input")

    if f".{output_ext}" not in valid_ext:
        sys.exit("Invalid output")

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    try:
        img = Image.open(input_file)

    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")

    size = shirt.size
    img = ImageOps.fit(img, size)

    img.paste(shirt, shirt)
    img.save(output_file)


if __name__ == "__main__":
    main()