#Compass Student Export to Seperate CSV for Barcode creation. Library Use
# Justin Clarke <justin@dev.justinclarke.me>

'''import csv
f=open('file.csv')
datareader = csv.reader(f, delimiter=',', quotechar='"')
headers = datareader.next()

datalist=[]
for row in datareader:
    data={}
    for i in range(4):
        data[headers[i]] = row[i]
    datalist.append(data)

for data in datalist:
    print(data)
'''

inFile = 'students.csv'
#inFile = $1

import os
import csv

import labels

f = open(inFile)
datareader = csv.reader(f, delimiter=',', quotechar='"')

headers = next(datareader)
datalist=[]
forms = {}

classForms = {}
for row in datareader:
    data={}
    for i in range(len(headers)):
        data[headers[i]] = row[i]

    #attempt to add the student into the specified FormGroup, or creates the FormGroup
    try:
        classForms[data['FormGroup']].append(data)
    except KeyError as e:
        classForms[data['FormGroup']] = []
        classForms[data['FormGroup']].append(data)

    #adds the FormGroup into a list, for use later
    forms[data['FormGroup']]=data['FormGroup']

#for each FormGroup, create a seperate CSV.
try:
    os.mkdir('out')
except FileExistsError as e:
    pass

for form, students in classForms.items():
    outFile = "out{}{}.csv".format(os.path.sep,form)
    print(outFile)
    #create file for FormGroup
    with open(outFile, 'w', newline='\n') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for student in students:
            writer.writerow(student)

            #create barcodes
            labels.gen_barcode(student["SussiId"], student["SussiId"])



    #create html
    html_file = labels.gen_html(form, students)
    labels.gen_pdf(html_file,"{}.pdf".format(form) )

#create PDFs


#print(classForms['Prep J'])
#print(classForms)
