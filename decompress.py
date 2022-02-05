'''
decompress.py

This file accepts an a7s file and zlib decompresses it. The
a7s file cannot be an archive. If the file is an archive,
you first need to extract it using RDAExplorerGUI.exe.

    https://github.com/lysannschlegel/RDAExplorer/releases

After running this script, the zlib decompressed (output) 
file needs to be converted from the propietary format to 
xml using FileDBReader.exe.

    https://github.com/anno-mods/FileDBReader/releases/latest

The command to decompress using FileDBReader from PowerShell
is:

        $ .\FileDBReader.exe decompress -f 'output_file' -c 2
'''
import zlib

# file to decompress from and write to
input_file = './data/data.a7s'
output_file = './data/data'

# read file and zlib decompress
str_object1 = open(input_file, 'rb').read()
str_object2 = zlib.decompress(str_object1)

# write decompressed file
with open(output_file, 'wb') as f:
    f.write(str_object2)
