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

#########EXCERSIZE ###########
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
# # # # # # # # # #  part 132 ( Advanced Lists) # # # # # # # # #
# # # # # # # # # #  part 133 ( Advanced Lists) # # # # # # # # #