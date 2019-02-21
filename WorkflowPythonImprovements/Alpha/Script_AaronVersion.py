import pymarc
from pymarc import MARCReader
from pymarc.field import Field
from pymarc import Record
from pymarc import Writer
import re

# create variables for input and output files
inputfile = open('Test.mrc', "rb")
outputfile = open("EbkScriptOutput.mrc", "ab")


# create an object for the MARC record
reader = MARCReader(inputfile)

# count records and print
count = 0
newCount = 0
otherCount = 0
for record in reader:
	count = count+1

# delete the 998 fields in the record
	record.remove_fields('998')
	record.add_field('998')
	for tempField in record.get_fields('998'): 
		if tempField is not None:
			newCount += 1

# Add 998 $a from online if cr in 007 or print if else
	for field in record.get_fields('007'): 
		if field.value().find('cr') >= 0:
			record['998'].add_subfield('a', 'MARCit')
			otherCount += 1
		'''else:
			record.add_field('998')
			otherCount += 1
			record.get_fields('998').add_subfield('a', 'MARCit from print')'''

	#outputfile.write(record.as_marc())

print('Total MARC records= ' + count)
print('Number of MARC records from electronic= ' + newCount)
print('Number of MARC records from print= ' + otherCount)

# close input and output files

# write record to new file

count = 0

for record in reader:
	for f in record.get_fields('998'):
		if f is not None:
			count += 1
print(count)


outputfileread.close()
'''



