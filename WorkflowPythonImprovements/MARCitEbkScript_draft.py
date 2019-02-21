import pymarc
from pymarc import MARCReader
from pymarc.field import Field

#how many records in file
with open('/home/rtillay/Documents/WorkflowPythonImprovements/sampleData/20180105.mrc', 'rb') as ebkImportFile:
  reader = MARCReader(ebkImportFile)
  num = 0
  for record in reader:
    num=(num + 1)
  print num

# minimal requirements = *mr*
# enhanced = *en*

# Step 1
# *en* How many records have a 998 field
with open('/home/rtillay/Documents/WorkflowPythonImprovements/sampleData/20180105.mrc', 'rb') as ebkImportFile:
    reader = MARCReader(ebkImportFile)
    for record in reader:
        if record['998'] is not None:
        	print(record['998'])

# *mr* Delete any existing 998 fields
ebkMARCExport=MARCReader(file('/home/rtillay/Documents/WorkflowPythonImprovements/sampleData/20180105.mrc'), to_unicode=True, force_utf8=True)

for ebkrecord in ebkMARCExport:
    if ebkrecord['998'] is not None:
         print ebkrecord.get_fields('998')[0].value()
         ebkrecord.remove_field(ebkrecord.getfields('998')[0])
         print '998 field removed'

# *en* How many records have a 998 field (should be 0 now)
with open('/home/rtillay/Documents/WorkflowPythonImprovements/sampleData/20180105.mrc', 'rb') as ebkImportFile:
    reader = MARCReader(ebkImportFile)
    for record in reader:
        if record['998'] is not None:
          print(record['998'])

