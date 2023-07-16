import pandas as pd
import numpy as np
import pandas as pd

# Read the Excel file and specify the sheet name/index
df = pd.read_excel("C:\\Users\\adish\\Dropbox\\Pure Path RPP validation\\RUN files\Plate -6 96 Well RPP AC Dil Pool 1 and 2.xlsx", sheet_name="Result", skiprows=19)

# Continue with your data processing or analysis


# Define the well ranges
well_ranges = {
    'Column A': [f'A{i:02d}' for i in range(1, 11)],
    'Column B': [f'A{i:02d}' for i in range(13, 23)],
    'Column C': [f'B{i:02d}' for i in range(1, 11)],
    'Column D': [f'B{i:02d}' for i in range(13, 23)],
    'Column E': [f'C{i:02d}' for i in range(1, 11)],
    'Column F': [f'C{i:02d}' for i in range(13, 23)],
    'Column G': [f'D{i:02d}' for i in range(1, 11)],
    'Column H': [f'D{i:02d}' for i in range(13, 23)],
    'Column I': [f'E{i:02d}' for i in range(1, 11)],
    'Column J': [f'E{i:02d}' for i in range(13, 23)],
    'Column K': [f'F{i:02d}' for i in range(1, 11)],
    'Column L': [f'F{i:02d}' for i in range(13, 23)],
    'Column M': [f'G{i:02d}' for i in range(1, 11)],
    'Column N': [f'G{i:02d}' for i in range(13, 23)],
    'Column O': [f'H{i:02d}' for i in range(1, 11)],
    'Column P': [f'H{i:02d}' for i in range(13, 23)],
    'Column Q': [f'I{i:02d}' for i in range(1, 11)],
    'Column R': [f'I{i:02d}' for i in range(13, 23)],
    'Column S': [f'J{i:02d}' for i in range(1, 11)],
    'Column T': [f'J{i:02d}' for i in range(13, 23)],
    'Column U': [f'K{i:02d}' for i in range(1, 11)],
    'Column V': [f'K{i:02d}' for i in range(13, 23)],
    'Column W': [f'L{i:02d}' for i in range(1, 11)],
    'Column X': [f'L{i:02d}' for i in range(13, 23)],
    'Column Y': [f'M{i:02d}' for i in range(1, 11)],
    'Column Z': [f'M{i:02d}' for i in range(13, 23)],
    'Column AA': [f'N{i:02d}' for i in range(1, 11)],
    'Column AB': [f'N{i:02d}' for i in range(13, 23)],
    'Column AC': [f'O{i:02d}' for i in range(1, 11)],
    'Column AD': [f'O{i:02d}' for i in range(13, 23)],
    'Column AE': [f'P{i:02d}' for i in range(1, 11)],
    'Column AF': [f'P{i:02d}' for i in range(13, 23)]
}

# Create a new DataFrame to hold the compiled data
df_compiled = pd.DataFrame()

# Iterate over the well ranges and compile the data
for col, wells in well_ranges.items():
    # Filter the DataFrame for the specified wells
    df_filtered = df[df['Well'].isin(wells)]
    
    # Extract the Cq values and assign them to the corresponding column
    cq_values = df_filtered['Cq'].values
    column_length = len(df_compiled)
    if len(cq_values) < column_length:
        cq_values = np.append(cq_values, [np.nan] * (column_length - len(cq_values)))
    
    df_compiled[col] = cq_values

# Save the compiled data to a new Excel file
df_compiled.to_excel('compiled_data_plate_6.xlsx', index=False)
