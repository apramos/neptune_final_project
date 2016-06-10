#! /usr/bin/env python
import re 
import sys 


InFileName= 'seq_newname.fasta' 
InFile= open(InFileName,'r')

OutFile=open('coding_frame.fasta','w')

for Line in InFile:
	if not Line.startswith('>'):
		SearchString='(ATG)(\w\w\w)+?(TAA|TGA|TAG)'  
		Results= list(re.finditer(SearchString, Line)) 
		CodFrame =''
		for Match in Results:
			if len(Match.group(0))>len(CodFrame):
				CodFrame=(Match.group (0))
		
		#print (CodFrame)
		OutFile.write(CodFrame+'\n')
	else:
		#print (Line)
		OutFile.write (Line)


InFile.close()
OutFile.close()

		
	



