import os
import subprocess
import scipy as sp
import numpy as np

class Shell(object):
    def __init__(self):
        pass
        
    def find_file(self,filename,directory=None):
        """
        find a file inside a given directory.  By default, the search starts
        in the home directory.
        """
        if directory is None:
            directory = subprocess.check_output("pwd").strip()

        command = "find " + directory + " -name \"" + filename + "\""
        output = os.popen(command).read().split("\n")
        output.pop() 
        return output
        
    def find_word(self,word,directory=None):
        """
        search the contents of all the files within a directory for a given
        word.
        """
        if directory is None:
            directory = subprocess.check_output("pwd").strip()

        command = "grep -nr " + word + " " + directory
        output = os.popen(command).read().split("\n")
        output.pop()
        return output

    def count_files(self, directory=None, r=True):
        """
        count the number of files within a given directory.

        Parameters
        ----------
        directory - string
        r - bool.  Whether or not you want to run the function recursively
        """
        if directory is None:
            directory = subprocess.check_output("pwd").strip()        

        if r:
            command = "find " + directory + " -type f | wc -l"
            return int(os.popen(command).read().split('\n')[0])
        else:
            command = "ls -l"
            count = 0
            output = os.popen(command).read().split("\n")
            output.pop()
            for line in output:
                if line[0] == "-":
                    count += 1
            return count

    def largest_files(self, directory=None, r=True, n=5):
        if directory is None:
            directory = os.popen("pwd").read().strip()
        
        if r:
            command = "du " + directory + " -a | sort -nr"
            items = os.popen(command).read().strip().split('\n')
            items = [i.split('\t') for i in items]
            
            files = []
            for i in xrange(len(items)):
                command = "ls -1 " + items[i][1] + " | wc -l"
                length = int(os.popen(command).read().strip())
                if length == 1:
                    files.append(items[i])
            if len(files) <= n:
                return files
            else:
                return files[:n]
        else:
            command = "ls -s | sort -k1r"
            files = os.popen(command).read().strip().split('\n')
            files = files[1:]
            files = [i.split() for i in files]
            if len(files) <= n:
                return files
            else:
                return files[:n]

    def largest(self,n,d=None):
        if d is None:
            d = os.popen('pwd').read.strip()
        command = "find " + d + " -type f"
        files = os.popen(command).read().split('\n')
        files.pop()
        split_files = np.array([os.popen("du " + f).read().strip().split('\t') for f in files])
        sizes = np.array(split_files[:,0],dtype=np.int32)
        sorted_index = sp.argsort(sizes)[::-1]
        return split_files[sorted_index][:n]
        
            
