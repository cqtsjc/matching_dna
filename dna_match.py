/*
Author: Amith Bhonsle
Created date: 06/09/2018
*/

from os import getcwd, path

__version__ = 0.0.1
__FILENAME__ = "dna_check input.txt"

__CUR_DIR__ = os.getcwd()
__FILEPATH__ = path.join(CUR_DIR, __FILENAME__)
if path.exists(__FILEPATH__):
    print("Found DNA sequence file")
else:
    print("DNS sequence file not found.\nMake sure the file is in the same directory.\nExiting....")