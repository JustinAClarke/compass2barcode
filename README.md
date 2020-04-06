# Compass to Barcode Creator.

## What is this?
This is a program to take the user export from Compass School Manager (People Manager, User Export) and create seperate scannable barcode sheets for use with library systems.
Note: this is using the SussiId as the barcode text.


## Install
Python 3
[wkhtmltopdf](http://wkhtmltopdf.org/)

### python-pip
python-barcode
jinja2
pdfkit

# Running the scripts
1. Place the file with the student export into the current working directory
2. Name this students file `students.csv`
3. Run the script `students.py`

Do the same as above for the staff but with the csv named `staff.csv`, and the python script `staff.py`
