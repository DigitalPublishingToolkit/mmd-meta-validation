#!/usr/bin/python

# A simple validation tool to check metadata in a MMD file
##########################################################
from collections import OrderedDict
import sys

# open the MMD document
file = open(sys.argv[-1])

# find metadata part of the file
metadata = OrderedDict()
for line in file:
	if line.find(':') != -1:	# check whether there is a ":" char in line
		key = line.split(':', 1)[0]
		value = line.split(':', 1)[1].lstrip().rstrip() # delete all white spaces at the beginning and the end
		metadata[key] = value
	elif (line.find(':') == -1) and (line != '\n'):
		lastKey = metadata.keys()[-1]
		lastValue = metadata.values()[-1]
		metadata[lastKey] = lastValue + ' ' + line.lstrip().rstrip() # delete all white spaces at the beginning and the end
	else:
		break

print
#check if there is any metadata
if len(metadata) == 0:
	sys.exit("There is no metadata in the document.\n")
else:
	print 'GENERAL'
	print 'There are', len(metadata), 'metadata in the document.\n'
	
#check mandatory metadata: title
def MandMDCheck( md, dict ):
	if md in dict:
		print ('"%s" is declared.' % md)		
	else:
		print ('There is no "%s" declared!' % md)
	return

#mandatory metadata
MandMD = ['Title', 'Author']
print 'MANDATORY METADATA'
for md in MandMD:
	MandMDCheck(md, metadata)
print

#check formatting of metadata
print 'METADATA FORMATTING'
# Is "type": "post" or "article"?
if (metadata['Type'] == 'Post') or (metadata['Type'] == 'Article'):
	print '"Type" is correctly declared.\n'
else:
	print '"Type" isn\'t correctly declared. Possible options are "Post" or "Article".\n'

# declare info about the document
print 'SUMMARY'
print ( "This %s was written by %s on the %s.\n" % (metadata['Type'], metadata['Author'], metadata['Date']) )

