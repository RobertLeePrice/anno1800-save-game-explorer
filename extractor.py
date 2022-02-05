'''
extractor.py

This file is designed to extract high level nodes from the 
decompressed save game xml file and output the result to a 
new xml file. 

The only purpose is to split the data into managable slices
while learning the syntax and testing data type conversions.
'''
import xml.etree.ElementTree as ET

# filename to extract from and write to
input_file = 'data.xml'
output_file = 'trade_route_data.xml'

# read input file into root object
tree = ET.parse(input_file)
root = tree.getroot()

# find subset of data by node and write to file
for node in root.findall('.//SessionTradeRouteManager'):
    children = ET.tostring(node, encoding='unicode')
    with open(output_file, 'w') as f:
        f.write(children)
