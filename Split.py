#This file is to split a dataframe based on a reference header and this list of values you care about in that specific column
#can be customised for .xlsx, .csv and .txt files 
#This function produces the resulting dataframe as a .xlsx file 

import pandas as pd 
df = pd.read_excel("Random.xlsx") 

# or alternativley for text or csv files 
# df = pd.read_csv("Random.text", demiliter = "|") 

#required for output 
column_name = "random header" 
df[column_name] = df[column_name].astype(str)

#list of references 
ls = ["random country1", "random country2"]

#filtering the data frame 
df= df.query("column_name in @ls")

output_path = "Randomly_filtered.xlsx" 
df.to_excel(output_path, sheetname = "whatever", index = False) 

      
