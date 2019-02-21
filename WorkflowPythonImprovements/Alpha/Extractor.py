"""  This script is intended to extract infromation from a MARC record and modify that information """

from pymarc import MARCReader, Record, Field

"""  Function Definitions """

""" Code Body """



with open("Test1.mrc", "rb") as file:
	reader = MARCReader(file)

	# count records
	count = 0
	for record in reader:
		if record['998'] is not None:
			count += 1

	print(count)

	# remove any existing 998 feilds
	for record in reader:
		record.remove_fields('998')

	# add test 998 field
	for record in reader:
		field = Field(tag = '998', subfields = ['a', 'Testing 1 ... 2'])
		record.add_field( field )
		print(record['998'])
