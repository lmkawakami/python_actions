import argparse
import requests
from urllib import parse

DEFAULT_COLOR = "blue"
DEFAULT_TEXT = "foo"
DEFAULT_VALUE = "bar"
DEFAULT_FILE_NAME = "badge.svg"

parser = argparse.ArgumentParser()
parser.add_argument("--color", help="hex value of the badge color, eg.#ff4545, blue, red")
parser.add_argument("--text", help="the text displayed on the badge, avoid using '#'")
parser.add_argument("--value", help="the value displayed on the badge")
parser.add_argument("--file_name", help="the output filename")

args = parser.parse_args()

color = args.color if args.color else DEFAULT_COLOR
color = parse.quote(color)
text = args.text if args.text else DEFAULT_TEXT
text = text.replace("-","_")
value = args.value if args.value else DEFAULT_VALUE
value = value.replace("-","_")
file_name = args.file_name if args.file_name else DEFAULT_FILE_NAME


url = f"https://img.shields.io/badge/{text}-{value}-{color}"
content = requests.get(url).text
print(url)
with open(file_name, 'w') as writer:
    writer.write(content)