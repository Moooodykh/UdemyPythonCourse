# ------------------------ Section 17: Working with PDFs and Spreadsheet CSV files is from part 129 to 133   -----------------------------

# # # # # # # # # #  part 129 ( 129. Introduction to PDFs and Spreadsheets with Python) # # # # # # # # #
#### JUST INTRODUCTION

# # # # # # # # # #  part 130 ( Working with CSV Files in Python) # # # # # # # # #
""" 
#CSV is a Comma Sperated Variables
#CSV contains ONLY the data, not macros,styling...etc

###PANDAS 
# is a full data analysis library which works with different types of data files not only CSV, Run visualization and analysis...etc
###OPENPYXL
# dedsigned specifcially for EXCEL, retain a lot of Excel functionality , support Excel formulas 
### GOOGLE SHEETS PYTHON API
#working with Google sheets, allow directly make changes to online hosted sheets, alot more complex


import os
import csv
current_directory = os.getcwd()
files_path = os.path.join(current_directory,'PythonCode\PDFs_Sheets')
print(files_path)
##############READING FROM CSV files ######################

######STEPS
# 1.Open the file
# 2.CSV.reader
# 3.Reformat it into a python object list of list

#1.
# Dealing with CSV example file
CSV_example = files_path+'\\'+'example.csv'
data = open(CSV_example,encoding='utf-8')
#### when you deal with files which has a different language or a seperated signs like @ ?...etc this called encoding.
# you will face ENCODING PROBLEM , SO YOU NEED TO ADD ENCODING TYPE as UTF-8

#2.
csv_data = csv.reader(data)
#3. 
data_lines = list(csv_data)
print(*csv_data)
######Exception has occurred: UnicodeDecodeError so we add "encoding='utf-8'"

#to go throough the data
# for line in data_lines:
#     print(line)

### typically the first row is the LABEL DATA
print(data_lines[0])
print(len(data_lines)) # it is 1001 divided to 1:LABEL data + 1000  information data

## printing the first 5 objects
for lin in data_lines[:5]:
    print(lin)

# to grab a specific item
print(data_lines[10])
# to grab a specific infomartion from that item as email
print(data_lines[10][3])

# grabbing all emails
for line in data_lines:
    print(line[3])

# we need to have a list of full names
fullnames = []
for line in data_lines[1:15]: #from the first name to number 15
    full_name = line[1] +' ' + line[2]
    fullnames.append(full_name)


print(*fullnames,sep='\n')

##############WRITING FROM CSV files ######################
#delimiter = seprator : NORMALLY COMMA','

# I WANT TO MAKE A NEW CSV file
# files are saved to : Result_of_the script folder

file_to_write = open('names.csv',mode='w',newline='\n')
# newline controls how universal newlines works (it only applies to text
# mode). It can be None, '', '\n', '\r', and '\r\n'.
csv_writer = csv.writer(file_to_write,delimiter=',')
csv_writer.writerow(['Id','FirstName','Lastname','email','gender','ip','city'])
ten_names = data_lines[1:10]
csv_writer.writerows(ten_names)
file_to_write.close()



#### EXCERSIZE TO READ AND WRITE FROM/TO CSV ####
import os,csv
desired_path = os.getcwd() +'\\' +'PythonCode\\PDFs_Sheets'
write_path = desired_path + '\\' + 'read_write_excersize'
os.chdir(desired_path)
### READING
csv_file = open('example.csv',mode='r',encoding='utf-8')
data_lines = csv.reader(csv_file)
data = list(data_lines)
Output_list = []

for row_data in data[:5]:
    Output_list.append(row_data[:4])
### WRITING
csv_output = open('output_save.csv',mode='w',newline='')
csv_writer = csv.writer(csv_output,delimiter=',')
csv_writer.writerows(Output_list)
csv_output.close()
"""

# # # # # # # # # #  part 131 ( Working with PDF Files in Python) # # # # # # # # #
""" 
# PDF :portable document format
#PYpdf2 library which will be used
import PyPDF2
import os
current_directory = os.getcwd()
files_path = os.path.join(current_directory,'PythonCode\PDFs_Sheets')
os.chdir(files_path)

file_under_work = open('Working_Business_Proposal.pdf',mode='rb') # Notice we read it as a binary with 'rb'
# Similar to the csv library, we open a pdf, then create a reader object for it. Notice how we use the binary method of reading , 
# 'rb', instead of just 'r'.
pdf_reader = PyPDF2.PdfFileReader(file_under_work)
print(pdf_reader.numPages) # getting the number of pages of that PDF dokument

page_one = pdf_reader.getPage(0)
page_one_text = page_one.extractText()
page_two = pdf_reader.getPage(1)
page_two_text =page_two.extractText()
page_three = pdf_reader.getPage(2)
page_three_text = page_three.extractText()

print('Page1: \n',page_one_text)
print('\nPage2: \n',page_two_text)
print('\nPage3: \n',page_three_text)

# file_under_work.close()



#### Adding to PDFs
# We can not write to PDFs using Python because of the differences between the single string type of Python, and the variety of fonts, placements, and other parameters that a PDF could have.
# What we can do is copy pages and append pages to the end.

## we need to have a page element to be able to attach it to a PDF 
print(type(page_three)) # it should be PyPDF2.pdf.PageObject

pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(page_three)
pdf_writer.addPage(page_two)
pdf_file_output = open('New_file.pdf',mode='wb')
pdf_writer.write(pdf_file_output)

file_under_work.close()

"""

######### EXCERSIZE ###########
# I want to read all text in that PDF and then CREAT a PDF with UPPERCASE OF ALL LETTERS
# Working_Business_Proposal.pdf

"""
import PyPDF2,os
result = ''
file_under_work = open('Working_Business_Proposal.pdf',mode='rb')
pdf_reader = PyPDF2.PdfFileReader(file_under_work)
# for pageNumber in range(pdf_reader.numPages):
#     page_element = pdf_reader.getPage(pageNumber)    
#     page_txt = page_element.extractText()
#     page_txt = page_txt.upper()
#     result = result + f'Page {pageNumber+1}:\n' +  page_txt +'\n'
# print(result)
print('*'*100)
page_zero = pdf_reader.getPage(0)
page_zero_txt = page_zero.extractText()
page_zero_txt = page_zero_txt.upper()

pdf_writer = PyPDF2.PdfFileWriter()
# pdf_writer.addPage(page_zero)
pdf_writer.insertPage(page_zero,index=0)
pdf_writer..insertPage(page_zero,index=1)
pdf_output = open('test_upper.pdf',mode='wb')
pdf_writer.write(pdf_output)
file_under_work.close()
"""


#
# # # # # # # # # #  part 132-133 ( PDFs and Spreadsheets Python Puzzle Exercise && SOLUTION) # # # # # # # # #

path =r'E:\PROGRAMMING\github\UdemyPythonCourse\PythonCode\PDFs_Sheets\Exercise_Files'
""" #### TASK1
# Task One: Use Python to extract the Google Drive link from the .csv file. 
# (Hint: Its along the diagonal from top left to bottom right).
# the answer looks like = 'https://drive.google.com/open?id=1G6SEgg018UB4_4xsAJJ5TdzrhmXipr4Q'

import os,csv
os.chdir(path)
output_result = ''
file_under_work = open('find_the_link.csv',mode='r',encoding='utf-8')
csv_reader = csv.reader(file_under_work)
csv_data = list(csv_reader)
# print(*csv_data,sep='\n\n')
line_counter = 0
for row in csv_data:
    output_result +=  row[line_counter]
    line_counter += 1

print(output_result)


#### TASK2
# Task Two: Download the PDF from the Google Drive link (we already downloaded it for you just in case you can't
#  download from Google Drive) and find the phone number that is in the document. Note: There are different
#  ways of formatting a phone number!
# You should get this phone number
# 505 503 4455
import os,re,PyPDF2
small_pattern = r'\d{3}'
pattern = r'\d{3}.\d{3}.\d{4}'
os.chdir(path)

pdf_file = open('Find_the_Phone_Number.pdf',mode='rb') 
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
output_txt = ''
print('--'*25)
for page in range(pdf_reader.numPages):
    page_object = pdf_reader.getPage(page)
    page_content = page_object.extractText()
    output_txt += page_content

# print(output_txt)
ItemFound = re.search(pattern,output_txt)
print(ItemFound.group())
"""


############### Merging PDF files
files_path=r'E:\PROGRAMMING\github\UdemyPythonCourse\PythonCode\PDFs_Sheets\Extrascripts'

""" import PyPDF2,os
os.chdir(files_path)

def pdf_merger(pdfs,output):
    # creating pdf file merger object 
    pdf_merger = PyPDF2.PdfFileMerger()

    # appending pdfs one by one 
    for pdf in pdfs:
        with open(pdf,mode='rb') as f:
            pdf_reader = PyPDF2.PdfFileReader(f)
            pdf_merger.append(f)
    
    # writing combined pdf to output pdf file
    with open(output,mode='wb') as f:
        pdf_merger.write(f)


def main():
    pdfs = ['Find_the_Phone_Number.pdf','Working_Business_Proposal.pdf']
    output = 'Combined_PDF_file.pdf'

    pdf_merger(pdfs,output)

if __name__ == "__main__":
    main()

"""
################### MERGING
# You can find information 
# https://realpython.com/creating-modifying-pdf/

""" #### 1. CONTACTENATING (append())
import os,PyPDF2
from pathlib import Path
print(Path.home())# show the user directory
print(os.getcwd())


pdf_merger = PyPDF2.PdfFileMerger()
report_path = files_path + '\\reports'
os.chdir(report_path)
for folder,sub_folders,files in os.walk(report_path):
    for f in files:
        pdf_file_full_path = folder + '\\' + f
        pdf_merger.append(pdf_file_full_path)

with open('Report.pdf',mode='wb') as output_file:
    pdf_merger.write(output_file) 

#### 2.MERGING (merge) ## you need to append first of all some PDF to the merger
merg_path = report_path + '\\merg'
pdf_pathes = []
for folder,sub_folders,files in os.walk(report_path):
    for f in files:
        pdf_file_full_path = folder + '\\' + f
        pdf_pathes.append(pdf_file_full_path)

pdf_merger_merge = PyPDF2.PdfFileMerger()
pdf_merger_merge.append(pdf_pathes[0])
pdf_merger_merge.merge(2,pdf_pathes[1])

with open('report_merged_method.pdf',mode='wb') as file_output:
    pdf_merger_merge.write(file_output)


####### ROTATING PAGES
# I will open expense_report1.pdf file and every even page I rotate that.
import os,PyPDF2
pdf_file = open('expense_report1.pdf',mode='rb')
pdfreader_obj = PyPDF2.PdfFileReader(pdf_file)

pdfwriter = PyPDF2.PdfFileWriter()
for page in range(pdfreader_obj.numPages):
    page_obj =pdfreader_obj.getPage(page)
    if page % 2 == 0:
        page_obj.rotateClockwise(90)
        pdfwriter.addPage(page_obj)
    else:
        pdfwriter.addPage(page_obj)

with open('Rotated_file.pdf',mode='wb') as output_rotated:
    pdfwriter.write(output_rotated)

pdf_file.close()
"""

################## Cropping Pages
""" 
import os,PyPDF2

working_path = os.getcwd() + '\\PythonCode\\creating-and-modifying-pdfs\\practice_files'
os.chdir(working_path)
# print(working_path)
pdf_file = open('half_and_half.pdf',mode='rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
first_page = pdf_reader.getPage(0)
page_text = first_page.extractText()

print(first_page.mediaBox)
# The .mediaBox attribute returns a RectangleObject. This object is defined in the PyPDF2 package and represents a rectangular area on the page.

# RectangleObject([0, 0, 792, 612]) represents a rectangular region with the lower-left corner at the origin,
#  a width of 792 points, or 11 inches, and a height of 612 points, or 8.5 inches. Those are the dimensions of 
#  a standard letter-sized page in landscape orientation, which is used for the example PDF of The Little Mermaid.
#  A letter-sized PDF page in portrait orientation would return the output RectangleObject([0, 0, 612, 792]).

print(first_page.mediaBox.lowerLeft)
print(first_page.mediaBox.lowerRight)
print(first_page.mediaBox.upperLeft)# TUPLES
print(first_page.mediaBox.upperRight)
print(first_page.mediaBox.upperRight[0])
print(first_page.mediaBox.upperRight[1])

# we change the upper left size 
first_page.mediaBox.upperLeft = (0,360)
print(first_page.mediaBox.upperLeft)# TUPLES
print(first_page.mediaBox.upperRight)

pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(first_page)
with open('cropped_page.pdf',mode='wb') as f_w:
    pdf_writer.write(f_w)

pdf_file.close()


### CROPPING RIGHT LEFT
import copy
import os,PyPDF2

pdf_file = open('half_and_half.pdf',mode='rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
first_page = pdf_reader.getPage(0)


left_side = copy.copy(first_page)
current_coords = left_side.mediaBox.upperRight
new_coords = (current_coords[0] / 2, current_coords[1])
left_side.mediaBox.upperRight = new_coords

right_side = copy.copy(first_page)
right_side.mediaBox.upperLeft = new_coords


pdf_writer2 = PyPDF2.PdfFileWriter()
pdf_writer2.addPage(left_side)
pdf_writer2.addPage(right_side)
with open("cropped_pages_2.pdf",mode="wb") as output_file:
    pdf_writer2.write(output_file)

pdf_file.close()

"""
###################### Encrypting and Decrypting PDFs
""" 
# You can add password protection to a PDF file using the .encrypt() method of a PdfFileWriter() instance. 
# It has two main parameters:
# user_pwd sets the user password. This allows for opening and reading the PDF file.
# owner_pwd sets the owner password. This allows for opening the PDF without any restrictions, including editing.


#####ENCRYPT
import os,PyPDF2
user_password = "SuperSecret"
owner_password = "ReallySuperSecret"


working_path = os.getcwd() + '\\PythonCode\\creating-and-modifying-pdfs\\practice_files'
os.chdir(working_path)
pdf_file = open('newsletter.pdf',mode='rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
pdf_writer = PyPDF2.PdfFileWriter()

for page in range(pdf_reader.numPages):
    Page_item = pdf_reader.getPage(page)
    pdf_writer.addPage(Page_item)

with open('Newsletter_encrypted.pdf',mode='wb') as fw:
    pdf_writer.encrypt(user_pwd=user_password,owner_pwd=owner_password)
    pdf_writer.write(fw)

pdf_file.close()

#####DECRYPT

import os,PyPDF2
user_password = "SuperSecret"
owner_password = "ReallySuperSecret"

pdf_file = open('Newsletter_encrypted.pdf',mode='rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
pdf_reader.decrypt(user_password)
pdf_writer = PyPDF2.PdfFileWriter()

for page in range(pdf_reader.numPages):
    Page_item = pdf_reader.getPage(page)
    pdf_writer.addPage(Page_item)

with open('Newsletter_after_decryption.pdf',mode='wb') as fw:
    pdf_writer.write(fw)

pdf_file.close() 
"""


###################### Creating a PDF File From Scratch

"""
###### X: lowerleft
###### Y: lowerleft

# Using the Canvas Class
# The main interface for creating PDFs with reportlab is the Canvas class,
#  which is located in the reportlab.pdfgen.canvas module.
import os
from reportlab.lib.units import inch,cm
from reportlab.lib.pagesizes import LETTER,A4,TABLOID
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.colors import blue,red,green

print(cm)
print(inch)
os.chdir(os.getcwd()+r'\PythonCode\Canvas')
canvas_obj = Canvas('hello.pdf',pagesize=(612.0, 792.0)) # empty PDF object with this size of points
# 1 inch = 72 points
# 1 cm = 28.2324 points

canvas_obj2 = Canvas('hello.pdf',pagesize=(8.5 * inch, 11 * inch)) # empty PDF object
canvas_obj3 = Canvas('hello.pdf',pagesize=LETTER) # empty PDF object

canvas_obj3.drawString(72,72,'Hello GUYS')
#x: The first specifies the distance from the left edge of the canvas
#y:the second specifies the distance from the bottom edge.
canvas_obj.save()

canvas = Canvas("font-example.pdf", pagesize=LETTER)
canvas.setFont("Times-Roman", 18)
canvas.drawString(1*inch,6*inch,'HELO HELLO HOW ARE YOU MAN WE LOVE YOU')
canvas.drawString(1*inch,6*inch,'HELO HELLO HOW ARE YOU MAN WE LOVE YOU')
canvas.save()

# There are three fonts available by default:
# "Courier"
# "Helvetica"
# "Times-Roman"

# Each font has bolded and italicized variants. Here’s a list of all the font variations available in reportlab:
# "Courier"
# "Courier-Bold"
# "Courier-BoldOblique"
# "Courier-Oblique"
# "Helvetica"
# "Helvetica-Bold"
# "Helvetica-BoldOblique"
# "Helvetica-Oblique"
# "Times-Bold"
# "Times-BoldItalic
# "Times-Italic"
# "Times-Roman"

canvas_courier = Canvas('Different_Fonts.pdf',pagesize=A4)
print(A4)

canvas_courier.setFont('Courier-Bold',size=16)
canvas_courier.setFillColor(blue)
canvas_courier.drawString(1*inch,4*inch,'Here is the "Courier-Bold" TEXT ')

canvas_courier.setFont('Helvetica-Bold',size=16)
canvas_courier.setFillColor(green)
canvas_courier.drawString(1*inch,8*inch,'Here is the "Helvetica-Bold" TEXT ')

canvas_courier.setFont('Times-Bold',size=16)
canvas_courier.setFillColor(red)
canvas_courier.drawString(1*inch,6*inch,'Here is the "Times-Bold" TEXT ')

canvas_courier.save()
"""

############################################ EXCERSIZE 
# go through both PDFs , find the phone number and then SAVE it as a head of the file in color BLUE
# then Each age of  Working_Business_Proposal.pdf will have a different FONT TYPE and FONT COLOR.
# THe FINAL RESULT PDF file is having even pages as normal and odd as verticals.
#THe PDF file need to be encrypted
# location = PythonCode\PDFs\Final_excesize
import os,PyPDF2,re
from reportlab.lib.colors import red,greenyellow,blueviolet,orange,green,blue
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import LETTER,A4
from reportlab.lib.units import inch
import textwrap #wrapping the code
from reportlab.pdfbase.pdfmetrics import stringWidth # measuring the lenth of the string


#access the files
files_directory = os.getcwd()+r'\\PythonCode\\PDFs\\Final_excesize'
os.chdir(files_directory)



def find_pdf_file_path(folder_path):
    '''
    Param:folder_path
    Output: List of full path of all PDFs
    '''
    paths = []    
    for folder,sub_folders,files in os.walk(folder_path):
        for fil in files:
            full_path = folder + '\\' + fil
            paths.append(full_path)
    return paths

list_of_pdfs = find_pdf_file_path(files_directory)


#Extract date from PDF file and search
def extract_data_from_pdfs(pdf_file):
    '''
    param:pdf file path
    output: dictionary which contain all data from that PDF (key = page number,value = text paragraph)
    '''
    pdf_content = {}
    # pdf_text = ''

    file_to_open = open(f'{pdf_file}',mode='rb')
    pdf_reader = PyPDF2.PdfFileReader(file_to_open)
    for page in range(pdf_reader.numPages):
        page_element = pdf_reader.getPage(page)
        page_text = page_element.extractText()
        pdf_content[page] = page_text
        # pdf_text = pdf_text + f'Page {page}:\n' + page_text
    file_to_open.close()
    
    return pdf_content

data_out_1 = extract_data_from_pdfs(list_of_pdfs[0])# first PDF file (search number)
data_out_2 = extract_data_from_pdfs(list_of_pdfs[1])# second pdf file , TEXT file

# print(len(data_out_2))
def pdf_file_with_its_own_data(list_of_pdfs):  
    '''
    param:list of PDFS
    output: dictionary contains each PDF file name attached to its content dict:(pdfname,content)
    '''
    pdfname_with_content = {}
    for pdf in list_of_pdfs:
        pdf_data = extract_data_from_pdfs(pdf)
        pdfname_with_content[pdf] = pdf_data
    return pdfname_with_content


# EVEN = normal ,ODD = vertical
def rotate_encrypt_pdf(pdf_file):
    '''
    param:PDF file
    output: PDF file , odd page numbers will be rotated and even page numbers will be normal
    param:PDF file
    output: Encrypted PDF file
    '''
    user_password = 'superNiceActivity'
    file_to_open = open(f'{pdf_file}',mode='rb')
    pdf_reader = PyPDF2.PdfFileReader(file_to_open)
    pdf_writer = PyPDF2.PdfFileWriter()
    for page in range(pdf_reader.numPages):
        page_element = pdf_reader.getPage(page)
        if page % 2 == 0:
            page_element.rotateClockwise(90)
            pdf_writer.addPage(page_element)
        else:
            pdf_writer.addPage(page_element)
    with open('Final_result.pdf',mode='wb') as fw:
        pdf_writer.encrypt(user_pwd=user_password) #ENCRYPTION PART
        pdf_writer.write(fw)

    file_to_open.close()



def serach_for_phone_number(dict_data):
    '''
    param : data from a file
    output: results that match the pattern (List)
    '''
    pattern = r'\d{3}.\d{3}.\d{4}'
    search_results = []
    for key in dict_data.keys():
        f = re.search(pattern,dict_data[key])
        if f != None:
            search_results.append(f)
    return search_results


search_output =  serach_for_phone_number(data_out_1)



#Build PDF from scratch
canvas = Canvas('New_PDF_file.pdf',pagesize=A4)
canvas.setFont("Courier-Bold",size=16)
canvas.setFillColor(blue)

for item in search_output:
    canvas.drawString(3*inch,11*inch  , item.group())

# coloring each page
for item in range(len(data_out_2)):
    
    if item == 0:
        textobject = canvas.beginText(1*inch,10*inch)
        textobject.setFillColor(red)
        textobject.setFont('Helvetica-Bold',size= 13)
        textobject.textLines(data_out_2[item])
        # canvas.showPage() # close the current page and start new one
        canvas.drawText(textobject)

    elif item == 1:
        textobject = canvas.beginText(1*inch,10*inch)
        textobject.setFont('Helvetica-Bold',size= 12)
        textobject.setFillColor(green)
        textobject.textLines(data_out_2[item])
        canvas.showPage() # close the current page and start new one
        canvas.drawText(textobject)

    elif item == 2:
        textobject = canvas.beginText(1*inch,10*inch)
        textobject.setFillColor(orange)
        textobject.setFont('Helvetica-Bold',size= 11)
        textobject.textLines(data_out_2[item])
        canvas.showPage() # close the current page and start new one
        canvas.drawText(textobject)
    elif item == 3:
        textobject = canvas.beginText(1*inch,10*inch)
        textobject.setFillColor(blueviolet)
        textobject.setFont('Helvetica-Bold',size= 10)
        textobject.textLines(data_out_2[item])
        canvas.showPage() # close the current page and start new one
        canvas.drawText(textobject)
    else:
        textobject = canvas.beginText(1*inch,10*inch)
        textobject.setFillColor(greenyellow)
        textobject.setFont('Helvetica-Bold',size= 9)
        textobject.textLines(data_out_2[item])
        canvas.showPage() # close the current page and start new one
        canvas.drawText(textobject)
canvas.save()

#ROTATION & ENCRYPTION 
rotate_encrypt_pdf('New_PDF_file.pdf')











#----------------------------------------------

        ###WRAPPER
        # wrapper = textwrap.TextWrapper(width=50)
        # words_list = wrapper.fill(data_out_2[item])
        # for row in words_list:
        #     print(row) 
        #     canvas.drawString(1*inch,10.5*inch,row)   
        #     canvas.drawString(1*inch,10.5*inch,'\n')   
