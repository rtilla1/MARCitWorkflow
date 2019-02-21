#!/usr/bin/python

import pymarc
from pymarc.field import Field

marcRecsIn_oclc_recs_1 = pymarc.MARCReader(file('3_oclc_recs_1_batch.mrc'), to_unicode=True, force_utf8=True)

for record_oclc_1 in marcRecsIn_oclc_recs_1:
	print record_oclc_1.get_fields('001')[0].value()
	record_oclc_1.remove_field(record_oclc_1.get_fields('001')[0]) 
	print '001 field removed'
