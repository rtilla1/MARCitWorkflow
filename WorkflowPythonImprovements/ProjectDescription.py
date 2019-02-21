# Beth's email:

# I know it’s touted as more powerful than MARCEdit, and there’s one particular sequence of processes that I’d like to eliminate from a bulk editing process we currently do for the weekly batches of MARCIt records. 
# It’s hard to describe the entire process without having MARCEdit open and running, but the end result is a local field (998) with three subfields that look like this:
 
# =998  \\$aMARCit$bsource record is online per 007 cr$cCONSER
# =998  \\$aMARCit from print$cnon-pcc
# =998  \\$aMARCit from print$cCONSER
# =998  \\$aMARCit$bsource record is online per 007 cr$cnon-pcc
# =998  \\$aMARCit$bsource record is online per 338$cnon-pcc
 
# Subfield a distinguishes between MARCit records based on print and those based on online records. 
# Subfield b shows if the “online” determination was made based on coding in 007 or 338. 
# Subfield c shows if the record is CONSER or not. 
# This is what Jeannette had devised, but even she wasn’t sure how necessary all of the data still was (so I may need to check with Gena about that). 
# I do know that we still keep stats on the number of CONSER records for e-resources.
 
# Those are the broad strokes, but if the process could be scripted in Python, it would streamline the workflow. 
# As it is, Frank has to go through half a dozen very confusing steps in MARCEdit to create the 998 field. 
# Because of the constraints of MARCit, working on a selection of records within a file results in the program closing once the edited selection is saved back to the main file. 
#This requires a user to repeatedly re-open the file and resume work, which greatly increases the potential for missed steps in the process.

# Project Requirements by Tillay:

# minimal requirements = *mr*
# enhanced = *en*


# Step 1
# *mr* Delete any existing 998 fields

# Step 2
# *mr* Create a 998 field with a $a for each record 
# *en* Report back how many records were edited
# *mr* Add a 998 $a of "MARCit" (only) if the 007 begins with "cr"
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

# Possibly useful links:
# https://groups.google.com/forum/#!searchin/pymarc/remove_field%7Csort:date/pymarc/t9WeuR2aYzA/Eth0iyZ54JYJ
# https://www.guru99.com/reading-and-writing-files-in-python.html
# https://www.oreilly.com/library/view/python-cookbook/0596001673/ch04s04.html
# https://github.com/lpmagnuson/pymarc-workshop
# https://github.com/edsu/pymarc/blob/master/pymarc/record.py
