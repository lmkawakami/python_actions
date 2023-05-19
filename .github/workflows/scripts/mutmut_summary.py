import xml.etree.ElementTree as ET

tree = ET.parse("./html_reports/mutmut/mutmut-results.xml")
root = tree.getroot()
node = root[0]
failures = int(node.get("failures"))
tests = int(node.get("tests"))
disabled = int(node.get("disabled"))
errors = int(node.get("errors"))
skipped = int(node.get("skipped"))
time = int(node.get("time"))

print(f"tests:{tests} | failures:{failures} | errors:{errors} | skipped:{skipped} | disabled:{disabled} | time:{time}")
