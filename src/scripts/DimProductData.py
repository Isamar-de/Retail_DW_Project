#import python libraries
import pandas as pd
import random
import csv

#input the number of rows that the csv file should have
num_rows = int(input("Enter the number of rows that should be generated: "))

#input the name of the csv file
csv_file = input("Enter the name of the csv file: ")

#details of the excel file that has the lookup data, file path and name, sheet name and column names where the data is present
excel_file_path_name = r'C:\Users\h700748235\OneDrive - Hofstra University\Documents\Personal\Project1\LookupFile.xlsx'
excel_sheet_name_product = "Raw Product Names"
product_column_name = "Product Name"
excel_sheet_name_category = "Product Categories"
category_column_name = "Category Name"

#fetch this sheet data in a dataframe
df = pd.read_excel(excel_file_path_name,sheet_name=excel_sheet_name_product)
df_cat = pd.read_excel(excel_file_path_name,sheet_name=excel_sheet_name_category)

#open the csv file
with open(csv_file,mode='w',newline='') as file:
    writer=csv.writer(file)

    #create the header
    header=['ProductName', 'Category', 'Brand', 'UnitPrice']

    #write the header to the csv file
    writer.writerow(header) 

    #loop and generate multiple rows
    for _ in range(num_rows):
        
        #generate a single row
        row = [
            df[product_column_name].sample(n=1).values[0], #product_name
            df_cat[category_column_name].sample(n=1).values[0], #category_name
            random.choice(['FakeLuxeAura', 'FakeUrbanGlow', 'FakeEtherealEdge', 'FakeVelvetVista', 'FakeZenithStyle']),
            random.randint(100,1000)
        ]


        #write the row to the csv file
        writer.writerow(row)


#print success statement
print(" the process completed succcessfully")