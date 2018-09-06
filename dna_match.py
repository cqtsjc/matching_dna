"""
Author: Amith Bhonsle
Created date: 06/09/2018
"""

from os import getcwd, path
from sys import exit, exc_info
from copy import deepcopy

__version__ = "0.0.2"
__FILENAME__ = "dna_check input.txt"

__CURDIR__ = getcwd()
__FILEPATH__ = path.join(__CURDIR__, __FILENAME__)

#Make sure that the input file exists.
if path.exists(__FILEPATH__):
    pass
else:
    print("DNS sequence file not found.\nMake sure the file is in the same directory.\nExiting....")
    exit(1)
    
class utils(object):
    def __init__(self):
        self.__UNMATCHED_SEQS__ = []
        self.__MATCHED_SEQS__ = {}
        self.__BASES_MATCH__ = {
            "A" : "T",
            "C" : "G",
            "T" : "A",
            "G" : "C"
            }
        
    def validate_line(self, line):
        """
        This function takes string as input and removes any spaces in it and converts it to DNA sequence.
        It also discards any empty strings.
        """
        try:
            if line and line != "\n":
                line = line.replace(" ", "")
                return line.strip()
            else:
                return None
        except Exception as err:
            print("Caught %s exception while validating line %s. Message: %s"%(err.__class__.__name__, line, str(err)))
            return None

    def find_dna_seq_match(self, CUR_SEQ):
        """
        This function takes a valid DNA seq string as input and checks if any match exists for it.
        """
        try:
            if not self.__UNMATCHED_SEQS__:
                self.__UNMATCHED_SEQS__.append(CUR_SEQ)
                return
            __TEMP_UNMATCHED_SEQS__ = deepcopy(self.__UNMATCHED_SEQS__)
            __TEMP_CUR_SEQ__ = list(CUR_SEQ)
            for UNMATCHED_SEQ in __TEMP_UNMATCHED_SEQS__:
                TEMP_UNMATCHED_SEQ = list(UNMATCHED_SEQ)
                if len(TEMP_UNMATCHED_SEQ) == len(CUR_SEQ):
                    for base in CUR_SEQ:
                        if self.__BASES_MATCH__[base] not in TEMP_UNMATCHED_SEQ:
                            self.__UNMATCHED_SEQS__.append(CUR_SEQ)
                            return
                        else:
                            TEMP_UNMATCHED_SEQ.remove(self.__BASES_MATCH__[base])
                            __TEMP_CUR_SEQ__.remove(base)
                    if TEMP_UNMATCHED_SEQ or __TEMP_CUR_SEQ__:
                        self.__UNMATCHED_SEQS__.append(CUR_SEQ)
                        return
                    else:
                        self.__UNMATCHED_SEQS__.remove(UNMATCHED_SEQ)
                        self.__MATCHED_SEQS__[UNMATCHED_SEQ] = CUR_SEQ
                        return
                else:
                    self.__UNMATCHED_SEQS__.append(CUR_SEQ)
        except Exception as err:
            print("Caught %s exception while finding DNA match for %s. Message: %s"%(err.__class__.__name__, CUR_SEQ, str(err)))
            print("At line: %s"%exc_info()[-1].tb_lineno)
            return None

    def get_results(self):
        try:
            if self.__UNMATCHED_SEQS__:
                print ("Output is: FALSE")
            else:
                print ("Output is: TRUE\n\nSince:-\n")
                for seq1, seq2 in self.__MATCHED_SEQS__.items():
                    print("%s matches with %s"%(seq1, seq2))
        except Exception as err:
            print("Caught %s exception while getting results. Message: %s"%(err.__class__.__name__,  str(err)))
            return None

if __name__ == "__main__":
    try:
        lib = utils()
        with open(__FILEPATH__, 'r')  as FILEOBJ:
            for line in FILEOBJ.readlines():
                VALID_SEQ = lib.validate_line(line)
                if VALID_SEQ:
                    lib.find_dna_seq_match(VALID_SEQ)
                else:
                    pass
        lib.get_results()
    except IOError as ioerr:
        print("Exception while accessing the input file. Meaasge: %s"%str(ioerr))
    except Exception as err:
        print("Caught %s exception. Message: %s"%(err.__class__.__name__, str(err)))
