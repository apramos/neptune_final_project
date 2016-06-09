#! /usr/bin/env python
import re 
import sys 


InFileName= 'seq_newname.fasta' 
InFile= open(InFileName,'r')

#OutFile=open('coding_frame.fasta','w')

for Sequence in InFile:
	if not Sequence.startswith('>'):
		SearchString='(ATG)(\w\w\w)+?(TAA|TGA|TAG)'  
		Results= list(re.finditer(SearchString, Sequence)) 
		CodFrame =''
		for Match in Results:
			if len(Match.group(0))>len(CodFrame):
				CodFrame=(Match.group (0))
		print (CodFrame)
	else:
		print (Sequence)



			#print(Match.group(0))
	





#	if Result > 1000:
#		print (Result)
		#print (key)
	"""	
		NewHeader='>'+ AcessDict[key]+'\n'
		NewHeader=NewHeader.replace(key,'')
		print (NewHeader)
		OutFile.write(NewHeader)
	else:
		print (Acession) 
		OutFile.write(Acession)
"""
