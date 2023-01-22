# -*- coding: utf-8 -*-
"""This script is used to check the existence, extension and content of a fasta file"""
from os.path import exists
# the exists function from the os.path checks the existance of a file
import sys
# sys provides to manipulate different parts of the py runtime environement
ADN_LIST=("A","C","G","T")#list of the possible DNA words
def read_dna(fastafile):
    """This function is used to check the contens of a fasta file"""
    with open(fastafile,"r") as file:# open the file
        lines = file.readlines()# reads all the contents from the given file
        counter = 0# initiate the counter of lines
        header = ""# empty header for the sequences name
        for line in lines:# reads line by line all the lines
            counter+= 1# for each line it starts counting
            if line[0] == ">": # if the 1st word in the file starts with '>'
                header = line.strip()# send the corresponding line to the header
            else:# in case the line doesn't start with '>'
                line = line.strip()# remove line breaks
                line = line.upper()# make the line uppercase
                column_counter = 0
                for char in line:# read character by character along the line
                    column_counter+= 1 # count characters
                    if char not in ADN_LIST: # if char is not in the DNA_list
                        print("\n"+char+" Is not a nucleotide, it is in line: "
                        +str(counter)+" and column: "+ str(column_counter)+
                        " and it corresponds to a sequence of: "+header[1:])
def check_fasta(fastafile):
    """This function is used to check the existence of the given file"""
    file_existance= exists(fastafile)#check the existance of the file in your computer
    if file_existance: #in case file exists
        ext= fastafile.split(".")[1]#get the words after the (.)
        fatsa_extension= ["fna","faa","fa","ffn","frn"] #check the extension of the file
        if ext not in fatsa_extension:
            print("This is not a fasta file: ("+fastafile +") please check the file extension!")
        else:
            read_dna(fastafile) #in this case use the function to read the fasta_file
    else:
        print("This file do not exist :"+ fastafile) #in case there is no file
if __name__=="__main__":
    for argument in sys.argv[1:]: #for each argument in sys.argv
        check_fasta(argument) #verify the existance and the extension of file


