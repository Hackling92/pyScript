"""
Created by Jacob Wilkes
pyscript is a simple script designed for use in CMPE315
this script is able to enscript files based on their name
and produce a matching pdf with the same name

NOTE: this program creates three folders if the do not already exist
Place vhd or vhdl files in the hvdl folder, pdfs will be saved to the
pdf folder and ps files will be stored in the ps folder.  This program
automatically overwrites the previous versions of the ps and pdf files.
"""

import os



def checkFolders():
    dirList = os.listdir(os.getcwd())
    
    if('pdf' not in dirList):
        os.mkdir('pdf')
    if('vhdl' not in dirList):
        os.mkdir('vhdl')
    if('ps' not in dirList):
        os.mkdir('ps')



def main():
    checkFolders()

    vhdlList = os.listdir(os.getcwd() + '/vhdl/')
    
    for file in vhdlList:
        fileName = file.split('.') #stip file extension off
        
        titleName = str(raw_input('Enter Header For [' + file + ']: '))

        # run enscript
        os.system('enscript --columns=2 --line-numbers --fancy-header --borders --landscape --pretty-print=vhdl --output ps/' + fileName[0] + '.ps --header "' + titleName + '" vhdl/' + file)
        
        # run ps2pdf
        os.system('ps2pdf ps/' + fileName[0] + '.ps pdf/' + fileName[0] + '.pdf')


main()
