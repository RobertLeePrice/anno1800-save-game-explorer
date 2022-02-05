# Anno1800 Save Game Explorer

The Anno1800 Save Game Explorer is a simple set of Python scripts for decompressing and converting data types from the save game files. 

## Install Tools

Before you get started, you'll need to download these community developed tools...

1. **RDA Explorer**: The RDA Explorer is a Windows Application that can read and save the RDA file format used in Anno 1404, 2070, 2205 and 1800. You can download the latest version here:  [Releases](https://github.com/lysannschlegel/RDAExplorer/releases)

2. **FileDBReader**: A simple command line unpacker, repacker and interpreter for proprietary Anno 1800 compression. You can download the latest version here: [Releases](https://github.com/anno-mods/FileDBReader/releases)


## Unpacking the Save Game Files

Once you download the tools above, find the path for the save game file you want to extract. On Windows, the save games are usually under a path similar to:
```
C:\Users\<Username>\Documents\Anno 1800\accounts
```
In these accounts folders, you'll find the save game files stored in a compressed *.a7s* file type.

1. Use ```RDAExplorerGUI.exe``` to open and extract the *.a7s* file. There should be 4 more *.a7s* files extracted: meta, header, gamesetup, and data. 
2. Decompress the ```data.a7s``` file using the zlib decompression script ```decompress.py```. You can change the name of the output file in the script. 
3. Decompress the output file from step (2) using ```FileDBReader.exe```. The PowerShell command is:

```powershell
.\FileDBReader.exe decompress -f '<<output_file>>' -c 2
```
Now, you should have a *.xml* file (Visual Studio Code is recommended to open). 

## Files

- ```extractor.py``` simple utility file for extracting a node and children from the save game xml. 
- ```parser.py``` includes some parsing functions to convert between data types 
- ```items.yaml``` a list of selected Anno1800 internal item IDs to English names
