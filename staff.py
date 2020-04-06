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

inFile = 'staff.csv'
#inFile = $1

import os
import csv

import labels

f = open(inFile)
datareader = csv.reader(f, delimiter=',', quotechar='"')

headers = next(datareader)
datalist=[]
forms = {}


for row in datareader:
    data={}
    for i in range(len(headers)):
        data[headers[i]] = row[i]
    datalist.append(data)

for staff in datalist:
    labels.gen_barcode(staff["SussiId"], staff["SussiId"])

html_file = labels.gen_html('staff', datalist, 'staff.tmpl')
labels.gen_pdf(html_file,"staff.pdf".format(datalist) )
#for staff in datalist:
'''
            #create barcodes
            labels.gen_barcode(student["SussiId"], student["SussiId"])



    #create html
    html_file = labels.gen_html(form, students)
    labels.gen_pdf(html_file,"{}.pdf".format(form) )

#create PDFs


#print(classForms['Prep J'])
#print(classForms)
'''
