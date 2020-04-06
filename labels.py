#Compass Student Export to Seperate CSV for Barcode creation. Library Use
# Justin Clarke <justin@dev.justinclarke.me>

import jinja2
import barcode
import pdfkit
import os

#create barcodes into a temp folder for each user
def gen_barcode(user,barcode_str):
    try:
        os.mkdir('tmp')
    except FileExistsError as e:
        pass
    #barcode script

    code128 = barcode.get('code128',barcode_str)
    code128.get_fullcode()
    filename = code128.save('tmp{}{}'.format(os.path.sep,user))

#generate html file for each class
def gen_html(class_name, class_list):
    try:
        os.mkdir('tmp')
    except FileExistsError as e:
        pass
    templateLoader = jinja2.FileSystemLoader(searchpath='./')
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = 'labels.tmpl'
    template = templateEnv.get_template(TEMPLATE_FILE)

    outputText = template.render(students = class_list)
    out_file = "tmp{}{}.html".format(os.path.sep,class_name)
    html_file = open(out_file,'w')
    html_file.write(outputText)
    html_file.close()
    return out_file

#save PDF of each class
def gen_pdf(in_file, out_file):
    pdfkit.from_file(in_file, out_file)
