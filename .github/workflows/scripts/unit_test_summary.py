import xml.etree.ElementTree as ET

tree = ET.parse("./html_reports/unit_test.xml")
root = tree.getroot()
node = root[0]
errors = int(node.get("errors"))
failures = int(node.get("failures"))
skipped = int(node.get("skipped"))
tests = int(node.get("tests"))

print(f"tests:{tests} | failures:{failures} | errors:{errors} | skipped:{skipped}")