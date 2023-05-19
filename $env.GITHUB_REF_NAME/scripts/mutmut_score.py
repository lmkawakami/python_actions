import xml.etree.ElementTree as ET

tree = ET.parse("./html_reports/mutmut/mutmut-results.xml")
root = tree.getroot()
failures = int(root.get("failures"))
tests = int(root.get("tests"))

score = ((tests - failures) / tests) * 100
print(f"{score:.1f}")