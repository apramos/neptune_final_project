#! /usr/bin/env python

import re, sys

def shorten_headers( in_name ):
	infile = open( in_name, "rU" )
	out = ""
	for line in infile:
		out = out + re.sub( 
			r">gi\|(\d+)\|[^|]+?\|([^|]+?)\.\d\|(.+)(\w+) (\w+)[\. ].+?$",
			#r"^>gi\|(\d+)\|[^|]+?\|[^|]+?\| (\w+) (\w+)[\. ].+?$", 
			r">\2", line )
			#r">\2_\3", line )
	

	return( out )

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print __doc__
		sys.exit( 0 )
	in_name = sys.argv[1]
	print shorten_headers( in_name )


	"""
	Shortens the header of NCBI fasta files to Genus_species_gi

usage:

python shorten_headers in.fasta > out.fasta


Written by Casey Dunn, Brown University, February 4, 2013.


"""