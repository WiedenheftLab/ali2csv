# ali2csv

	Author: Murat Buyukyoruk
      	Associated lab: Wiedenheft lab

        ali2csv help:

This script is developed to convert a multiple sequence alingment to a CSV file. 

tqdm is required to provide a progress bar since some multifasta files can contain long and many sequences.
        
Syntax:

        python ali2csv.py -i demo.fasta -l demo_sub_list.txt -o demo_sub_list.fasta

seq_fetch dependencies:
	pandas                                              refer to https://pandas.pydata.org/
	tqdm                                                refer to https://pypi.org/project/tqdm/
	
Input Paramaters (REQUIRED):
----------------------------
	-i/--input		FASTA			Specify a MSA fasta file.

	-o/--output		output file	    Specify a output file name that should contain CSV output.
	
Basic Options:
--------------
	-h/--help		HELP			Shows this help text and exits the run.

