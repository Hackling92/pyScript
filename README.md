# pyScript
A simple program designed to automate the workflow of creating PDFs for the CMPE-315 class at UMBC

This program is designed for python 2.6.6, this is the version provided on the UMBC GL server.

USAGE:
  python pyscript.py
  
NOTE:
  On the first run of the program three folders will be created, put any vhd/vhdl files you wish to enscript 
  into the vhdl folder.  Any ps files created will be placed into the ps folder and any pdfs created will be
  placed into the pdf folder.  For each file processed you will be asked for the header you wish to insert at
  the top of the file.
  
  Folders are not currently supported inside of the vhdl folder, if you wish to add this feature please add a
  pull request.
