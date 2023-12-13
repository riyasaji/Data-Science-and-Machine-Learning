import pandas as pd
# Load the CSV file into a DataFrame
df = pd.read_csv('sales_data.csv')
print("CSV FILE: ")
print(df)
print(" ")
# Get the number of rows and columns
num_rows, num_columns = df.shape
print("Number of Rows: ",num_rows)
print("Number of Columns: ",num_columns)
# Calculate the sum of the "Revenue" column
revenue_sum = df['Revenue'].sum()
print("The sum of Revenue column ",revenue_sum)
