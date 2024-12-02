# usr/bin/env-python3
'''

Plot the TN and TP concetrations

Author  : albert nkwasa
Contact : albert.nkwasa@vub.be / nkwasa@iiasa.ac.at
Date    : 2024.01.10

'''

import os
import pandas as pd
import matplotlib.pyplot as plt

# Define input folder and output folder for figures
# Change this to your input folder path
input_folder = ''
output_folder = ''

# Create 'figures' folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    # Process only CSV files
    if filename.endswith('.csv'):
        # Read the CSV file
        file_path = os.path.join(input_folder, filename)
        df = pd.read_csv(file_path)

        # Check if required columns are present
        if 'Date' in df.columns and 'Value' in df.columns and 'Value_obs' in df.columns:
            # Plot the data
            plt.figure(figsize=(10, 6))
            plt.plot(pd.to_datetime(df['Date']),
                     df['Value'], label='Simulated concetration', color='blue', linewidth=1)
            plt.scatter(pd.to_datetime(
                df['Date']), df['Value_obs'], label='Observed concentration', color='red', s=8, edgecolors='purple', alpha=0.7)
            plt.xlabel('Date')
            plt.ylabel('TN (mg/L)')
            plt.title(f'{filename[:-9]}')
            plt.legend()

            # Save the plot to the 'figures' folder with the same filename but as PNG
            output_file = os.path.join(
                output_folder, f'{os.path.splitext(filename)[0]}.png')
            plt.savefig(output_file)
            plt.close()

        else:
            print(
                f"Skipping {filename} as it does not contain required columns.")
