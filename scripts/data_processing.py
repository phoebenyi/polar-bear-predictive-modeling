import pandas as pd
import numpy as np

# File paths
input_file_chukchi = 'data/Chukchi Sea ice data.txt'
input_file_southern = 'data/Southern Beaufort Sea ice data.txt'
output_file = 'processed_data/processed_population_dynamics_data_with_trends.csv'

# Load raw data
chukchi_data = pd.read_csv(input_file_chukchi, delim_whitespace=True, header=None, 
                           names=['YEAR', 'DAY', 'SEA_ICE_EXTENT', 'SEA_ICE_AREA'])
southern_data = pd.read_csv(input_file_southern, delim_whitespace=True, header=None, 
                            names=['YEAR', 'DAY', 'SEA_ICE_EXTENT', 'SEA_ICE_AREA'])

# Add region columns
chukchi_data['REGION'] = 'Chukchi'
southern_data['REGION'] = 'Southern Beaufort'

# Combine datasets
combined_data = pd.concat([chukchi_data, southern_data], ignore_index=True)

# Add trend features
combined_data['DAY_SIN'] = np.sin(2 * np.pi * combined_data['DAY'] / 365)
combined_data['DAY_COS'] = np.cos(2 * np.pi * combined_data['DAY'] / 365)
combined_data['SEA_ICE_EXTENT_7D_AVG'] = combined_data.groupby('REGION')['SEA_ICE_EXTENT'].transform(lambda x: x.rolling(7, min_periods=1).mean())
combined_data['SEA_ICE_AREA_7D_AVG'] = combined_data.groupby('REGION')['SEA_ICE_AREA'].transform(lambda x: x.rolling(7, min_periods=1).mean())
combined_data['SEA_ICE_EXTENT_DIFF'] = combined_data.groupby('REGION')['SEA_ICE_EXTENT'].diff()
combined_data['SEA_ICE_AREA_DIFF'] = combined_data.groupby('REGION')['SEA_ICE_AREA'].diff()

# Save processed data
combined_data.to_csv(output_file, index=False)
print(f"Processed data saved to {output_file}")
