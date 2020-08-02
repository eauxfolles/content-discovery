# content-discovery
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)

PoC/Alpha of a tool written in Python to support with "Content Discovery" during mapping of a web applications/sites.

Function: Tool loads external file including names of files or folder which should be discovered. A target list is created consisting of a combination of the target URL and the possible files or folders. Probing is conducted and response displayed for each mix.  

***Usage:*** "condisc.py -option url [dictionary]"

Where: 
- "-option" is either "-files" or "-folders"
- "url" is the target URL including identifier for the used protocol (e.g. https://www.example.com)
- "dictionary" is the name of an optional dictionary to be used (located in same folder as the tool)

Two dictionaries (one for files, one for folders) are available to proof functionality. 
