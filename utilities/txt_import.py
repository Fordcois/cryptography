from pathlib import Path

def read_txt(txtfile):
    txtfile_path = Path(__file__).parent.parent / txtfile
    with open(txtfile_path, 'r') as file:
        # Read lines, strip whitespace, and remove empty lines, then join into a single string
        return ' '.join([line.strip() for line in file if line.strip() != ''])