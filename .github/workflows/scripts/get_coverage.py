import xml.etree.ElementTree as ET

def main():
    tree = ET.parse('./html_reports/code_coverage/cov.xml')
    root = tree.getroot()
    cov_percent = float(root.attrib['line-rate'])*100
    print(f'{cov_percent:.2f}%')
    return f'{cov_percent:.2f}%'

if __name__ == '__main__':
    main()