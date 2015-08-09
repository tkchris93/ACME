import os
import subprocess
import scipy as sp
import numpy as np

class Shell(object):
    def __init__(self):
        pass
        
    def find_file(self,filename,directory=None):
        """
        Find a file inside a given directory.  By default, the search starts
        in the current directory.
        """        
        if directory is None:
            directory = "."
            
        command = "find " + directory + " -name \"" + filename + "\""
        files = subprocess.check_output(command,shell=True).split('\n')
        files.pop()
        return files
        
    def find_word(self,word,directory=None):
        """
        search the contents of all the files within a directory for a given
        word.  By default, the search starts in the current directory
        """
        if directory is None:
            directory = "."

        command = "grep -nr " + word + " " + directory
        files = subprocess.check_output(command,shell=True).split('\n')
        files.pop()
        return files

    def largest_files(self,n,d=None):
        if d is None:
            d = '.'
        command = "find " + d + " -type f"
        files = subprocess.check_output(command, shell=True).split('\n')
        files.pop()
        split_files = np.array([subprocess.check_output('du ' + f, shell=True).strip().split('\t') for f in files]) 
        sizes = np.array(split_files[:,0],dtype=np.int32)
        sorted_index = sp.argsort(sizes)[::-1]
        return split_files[sorted_index][:n]
        
            
