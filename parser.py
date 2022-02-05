'''
parser.py

This is the main parsing functionality for extracting data
from the xml save games and converting data types. 
'''
import yaml
import xml.etree.ElementTree as ET

# input files to parse
input_config_file = 'items.yaml'
input_data_file = 'trade_route_data.xml'

# read item GUID to name conversions from file
with open(input_config_file) as f:
    items_config = yaml.load(f, Loader=yaml.FullLoader)

# error holder arrays
item_lookup_fails = []


# data type conversion functions
def binary_to_bool(h: str) -> bool:
    '''
    Converts the binary representation of a boolean 
    ('00', '01') to a Python boolean.

    Args:
        h (str): '00' or '01'.

    Returns: 
        bool: The return value, True or False.

    Example: 
        $ binary_to_bool('01') 
            -> True
    '''
    return bool(int(h))


def hex_to_str(h: str) -> str:
    '''
    Converts a hexadecimal string to a human-
    readable string. 

    Args:
        h (str): A hexadecimal string.

    Returns: 
        str: A human-readable text string.

    Example: 
        $ hex_to_str('4F006C006400200057006F0072006C006400') 
            -> 'Old World'
    '''
    return bytes.fromhex(h).decode('utf-16-le')


def str_to_hex(s: str) -> str:
    '''
    Converts a human-readable text string to 
    a hexadecimal string. 

    Args:
        s (str): A human-readable text string.

    Returns: 
        str: A hexadecimal string.

    Example: 
        $ str_to_hex('Essen') 
            -> '45007300730065006e00'
    '''
    return s.encode('utf-16-le').hex()


def hex_to_int16(h: str) -> int:
    little_hex = bytearray.fromhex(h)
    little_hex.reverse()
    str_little = ''.join(format(x, '02x') for x in little_hex)
    return int(str_little, 16)


def hex_to_item(h: str) -> str:
    little_hex = bytearray.fromhex(h)
    little_hex.reverse()
    str_little = ''.join(format(x, '02x') for x in little_hex)
    item_lookup = items_config.get(int(str_little, 16))

    if item_lookup is not None:
        item_name = item_lookup.get('english_text')
    else:
        if int(str_little, 16) not in item_lookup_fails:
            item_lookup_fails.append(int(str_little, 16))
        item_name = None

    return item_name


# assign tag name to data type converter
converters = {
    'IsDefaultName': binary_to_bool,
    'IsLoading': binary_to_bool,
    'HasTradeRights': binary_to_bool,
    'Name': hex_to_str,
    'ProductGUID': hex_to_item,
    'Amount': hex_to_int16,
    'BinaryData': hex_to_str,
}

# load xml file data in to tree object
tree = ET.parse(input_data_file)

# iterate through elements in xml tree
for elem in tree.iter():
    if elem.tag in converters:
        elem.text = converters[elem.tag](elem.text)
        # !!! warning - this print statement can be extremely large on a full xml file
        print(f'{elem.tag}: {elem.text}')

# print missing item IDs to be added to items.yaml
for f in item_lookup_fails:
    print(f'Could not find item with ID {f}.')
