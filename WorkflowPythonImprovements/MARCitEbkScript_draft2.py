import pymarc

# minimal requirements = *mr*
# enhanced = *en*

# create output MARC file

outputfile = open('/home/rtillay/Documents/PythonScripts/WorkflowPythonImprovements/sampleData/EbkScriptOutput.mrc','wb')

# assess how many records in file
with open('/home/rtillay/Documents/PythonScripts/WorkflowPythonImprovements/sampleData/20180105.mrc', 'rb') as ebkImportFile:
  reader = MARCReader(ebkImportFile)
  num = 0
  for record in reader:
    num=(num + 1)
  print num

# Step 1
# *en* How many records have a 998 field
with open('/home/rtillay/Documents/PythonScripts/WorkflowPythonImprovements/sampleData/20180105.mrc', 'rb') as fh:
    reader = MARCReader(fh)
    for record in reader:
        if record['998'] is not None:
          print(record['998'])

# *mr* Delete any existing 998 fields
  with open('/home/rtillay/Documents/PythonScripts/WorkflowPythonImprovements/sampleData/20180105.mrc', 'rb') as ebkImportFile:
    reader = MARCReader(ebkImportFile)
    for record in reader:
      if record['998'] is not None:
        record['998'] = None

# Write to output file
  outputfile.write(record.asMARC21())
  outputfile.close

# *en* How many records have a 998 field (should be 0 now)
  with open('/home/rtillay/Documents/PythonScripts/WorkflowPythonImprovements/sampleData/EbkScriptOutput.mrc', 'rb') as fh:
      reader = MARCReader(fh)
      for record in reader:
          if record['998'] is not None:
            print(record['998'])

# Step# *mr* Create a 998 field with a $a for each record 
# *en* Report back how many records were edited
# *mr* Add a 998 $a of "MARCit" (only) if the 007 begins with "cr"
# with open('/home/rtillay/Documents/PythonScripts/WorkflowPythonImprovements/sampleData/20180105.mrc', 'rb') as fh:
#	reader = MARCReader(fh)
#	record = next(reader)
#	record['998']['a'] = 'MARCit'

# *en* Report back how many records were edited
# *mr* Add a 998 $a of "MARCit from print" if the 007 begins with anything but "cr "
# *en* Report back how many records were edited

# Step 3
# *mr* Add a 998 $b "source record is online per 007 cr" if 007 begins with "cr"
# *en* Report back how many records were edited
# *mr* Add a 998 $b "source record is online per 338" if 338 includes "online"
# *en* Report back how many records were edited

# Step 4
# *mr* Add a $c "CONSER" if 008 byte 39 is c
# *en* Report back how many records were edited
# *mr* Add a $c "non-pcc" if 008 byte 39 is d
# *en* Report back how many records were edited

# Step 5
# *en* Report back total number of records
# *en* Report back total number 998 fields
# *en* Report each unique 998 field and how many of that field the file contains
# *mr* Save as "998 field edited by Python process"
