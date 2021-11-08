#import open source python library to perform data manipulation
import pandas as pd

#import json
import json


#Read CSV file from path in my computer
#in my case C:\Users\Diana Albarracin\Desktop\CO2Emission_LifeExp.csv
df = pd.read_csv (r'C:\Users\Diana Albarracin\Desktop\CO2Emission_LifeExp.csv') #change to the path where you saved the file

#Check if the data set is empty or has only one row (category names) and show error if this is the case
if (df.empty):
    print("Error: Data set is empty")
    
     

#CHECKPOINT 5  
#Summarize data before modification: Number of rows per column and number of columns of datafile

#store number of rows in num_rows
num_rows = len(df)

#store number of rows per column in num_rows_col
num_rows_col = df.count()

#Store number of columns in num_col

#Getting shape of df
shape = df.shape
num_col = shape[1]
#source of code for shape [1]
  
# Printing number of rows and number of columns of datafile
print('\033[92m' + '\033[1m'+ '\033[4m'+'Summary of data set before modification:' + '\033[0m')
print('\033[1m'+'Number of columns in data file:'+'\033[0m', num_col)
print('\033[1m'+'Number of rows in data file:'+'\033[0m', num_rows)
# Source to format the print to bold and different color [2]

#Print name of column and number of rows in that column
print('\033[1m'+'Number of rows in each category: '+'\033[0m', num_rows_col, sep='\n')
#source of code for separating the print statement [3]



#CHECKPOINT 3
#Modify the data file

#Delete the YearlyChange column in the data file
df.pop('YearlyChange')

#Store number of columns in modified data file new_num_col

#Getting shape of df
shape_mod = df.shape
new_num_col = shape_mod[1]

#check that the column was deleted and if not print an error
if (num_col-new_num_col!=1):
    print("Error: Modification of data file was not succesful")

    

#CHECKPOINT 5
#Summarize data after modification: Number of rows per column and number of columns of datafile

#store number of rows in new_num_rows
new_num_rows = len(df)

#store number of rows per column in new_num_rows_col
new_num_rows_col = df.count()

# Printing number of rows and number of columns of datafile
print('\033[92m' + '\033[1m'+ '\033[4m'+'Summary of data set after modification:' + '\033[0m')
print('\033[1m'+'Number of columns in data file:'+'\033[0m', new_num_col)
print('\033[1m'+'Number of rows in data file:'+'\033[0m', new_num_rows)

#Print name of column and number of rows in that column
print('\033[1m'+'Number of rows in each category: '+'\033[0m', new_num_rows_col, sep='\n')




#CHECKPOINT 2

#convert CSV file to JSON 
df2 = df.to_json("CO2Emission_LifeExp.json") 
#source of code for converting CSV to JSON [4]

#Save it onto your desktop
df.to_json(r'C:\Users\Diana Albarracin\Desktop\CO2Emission_LifeExp.json') #change to your path

#Check that the file was converted to JSON if not throw an error
with open('CO2Emission_LifeExp.json', 'r') as openfile:
    try:
        json_object = json.load(openfile)
    except ValueError:
        print ("Error: unable to convert to Json")
#source of code to valiidate if the file is a JSON file [5]


#Sources:
#[1] https://www.geeksforgeeks.org/count-number-of-columns-of-a-pandas-dataframe/#:~:text=Shape%20property%20returns%20the%20tuple%20representing%20the%20shape,get%20the%20number%20of%20columns%20in%20the%20df.
#[2] https://www.delftstack.com/howto/python/python-bold-text/#:~:text=To%20print%20the%20bold%20text%2C%20we%20use%20the,print%20statement%20will%20keep%20print%20the%20bold%20text.
#[3] https://realpython.com/python-print/
#[4] https://datatofish.com/csv-to-json-string-python/#:~:text=You%20may%20use%20the%20following%20template%20in%20order,steps%20to%20apply%20the%20above%20template%20in%20practice.
#[5] http://www.pythonpandas.com/reading-and-writing-json-to-a-file-in-python/#:~:text=Writing%20JSON%20to%20a%20file%20in%20python%20,%20%20numbers%20%203%20more%20rows%20
