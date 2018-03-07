# import libraries

import os, shutil, re

# create date patten to match file names

datePattern = re.compile(r"""^(.*?)
	((18|19)\d\d)-
	((0|1)\d)-
	((0|1|2|3)\d)-
	(\d\d\d)
	(.*?)
	([.]tif$)
        """, re.VERBOSE)
# edPart (0\d) # this will change if the edition is in a different place or if the edition is not included in the filename

# loop over files in working directory

for issueFileName in os.listdir('.'):
	mo = datePattern.search(issueFileName) #change from search to match

	if mo == None:
		continue

	# beforePart = mo.group(1) not necessary for the issueFolderName identification
	yearPart = mo.group(2)
	monthPart = mo.group(4)
	dayPart = mo.group(6)
	# edPart # should this be included?
	# afterPart # which group number?

	issueFolderName = yearPart + monthPart + dayPart + "01/"

	absWorkingDir = os.path.abspath('.')
	issueFileName = os.path.join(absWorkingDir, issueFileName)
	issueFolderName = os.path.join(absWorkingDir, issueFolderName)

	print("Moving '%s' to '%s'..." % (issueFileName, issueFolderName))
	shutil.move(issueFileName, issueFolderName)
