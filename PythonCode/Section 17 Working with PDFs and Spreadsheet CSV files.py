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








# # # # # # # # # #  part 131 ( Advanced Dictionaries) # # # # # # # # #
# # # # # # # # # #  part 132 ( Advanced Lists) # # # # # # # # #
# # # # # # # # # #  part 133 ( Advanced Lists) # # # # # # # # #