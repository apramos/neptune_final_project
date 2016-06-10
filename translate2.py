#! /usr/bin/env python
import re 
import sys 

codonDict = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

InFileName= 'coding_frame.fasta' 
InFile= open(InFileName,'r')

OutFile=open('protein_seq.fasta','w')

for Line in InFile:
	if not Line.startswith('>'):
		for Num in range(0,len(Line)/3): #goes through the seq one character each time until the end (defined by the lenght of seq)
			#print (Line[3*Num:(3*Num+3)]) #prints num+3 so that we can go 3 by 3
			codon=(Line[3*Num:(3*Num+3)])
			protein=''
			if codon in codonDict:
				protein=(codonDict[codon])
				OutFile.write(protein)
			else:
				#print ('x')
				OutFile.write('X')
		OutFile.write('\n')	
	else:
		#print (Line)
		OutFile.write(Line)






InFile.close()
OutFile.close()


		
	



