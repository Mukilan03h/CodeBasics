import pandas as pd
import os
# Load the CSV files into pandas DataFrames
dim_customer = pd.read_csv('F:\\CodeBasics\\C8_Input_Files\\dim_customers.csv')
fact_spends = pd.read_csv('F:\\CodeBasics\\C8_Input_Files\\fact_spends.csv')

# Merge the tables on the 'customer_id' column using an inner join
merged_table = pd.merge(dim_customer, fact_spends, on='customer_id', how='inner')

# Specify the path to save the merged table as a new CSV file
output_path = 'F:\\CodeBasics\\C8_Input_Files\\Dexp\\merged'

# Check if the directory exists, create it if not
output_directory = os.path.dirname(output_path)
os.makedirs(output_directory, exist_ok=True)

# Save the merged table as a new CSV file
merged_table.to_csv(output_path, index=False)

# Display progress
print("Merged table saved successfully to:", output_path)
