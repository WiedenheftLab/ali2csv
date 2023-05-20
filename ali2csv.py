#!/usr/bin/python

from Bio import SeqIO
import argparse
import os
import sys
import subprocess
import pandas as pd
import textwrap

try:
    from tqdm import tqdm
except ImportError, e:
    print "tqdm module is not installed! Please install tqdm and try again."
    sys.exit()

parser = argparse.ArgumentParser(prog='python ali2csv.py',
      formatter_class=argparse.RawDescriptionHelpFormatter,
      epilog=textwrap.dedent('''\

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

	
      	'''))
parser.add_argument('-i', '--input', required=True, type=str, dest='filename',
                        help='Specify a MSA fasta file.\n')

parser.add_argument('-o', '--output', required=True, dest='out',
                        help='Specify a output file name that should contain CSV output.\n')

results = parser.parse_args()
filename = results.filename
out = results.out

seq_id_list = []
seq_list = []
seq_description_list = []

os.system('> ' + out)

proc = subprocess.Popen("grep -c '>' " + filename, shell=True, stdout=subprocess.PIPE, )
length = int(proc.communicate()[0].split('\n')[0])

data = pd.DataFrame([])

with tqdm(range(length), desc = 'Reading...' ) as pbar:
    for record in SeqIO.parse(filename, "fasta"):
        pbar.update()
        seq_id_list.append(record.id)
        seq_list.append(record.seq)
        seq_description_list.append(record.description)
        seq_parse = list(record.seq)
        seq_parse.insert(0,record.description)

        df = pd.Series(seq_parse)

        row_df = pd.DataFrame([df])

        data = pd.concat([data, row_df], ignore_index=True)

print data
data.to_csv(out,sep='\t', index = False)





