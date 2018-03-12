# cleaning

This document contains regular expressions to remove uneccessary folder names.

## remove date

\d\d[/]\d\d[/]\d\d\d\d

## remove time
\d\d[:]\d\d (PM)


## remove file size -- may need to remove leading zeros (double check)

((\d+)[,])*(\d+)[,](\d+)

## remove title information 

\d\d\d[-]\w\w\w[-]

## remove sequence and trailing info and replace with edition number

(\d+)[-]((single)|(double))[.](tif)

## remove duplicates

copy to Excel
Data>Remove Duplicates

## remove line break

Copy back to Notepad++, Replace "Find what" "\n" Replace with " " [whitespace]. *Note: There may be an error in between copying such that linebreaks do not exist. If this is the case, in Excel, add a whitespace to the beginning of the string and then copy back to Notepad++.*


*Note: There may exist a file that does not follow the standard naming structure, for example in Farmer's Weekly Review, there were files that followed a naming convention such as, "039-FWR-1934-10-31-M01-single.tif." The current batch creation of folders does not recognize this, so be sure to check before running the .bat file or .py file.*

