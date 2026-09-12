import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

print("--- Power-to-Methane (PtM) Machine Learning Optimization Pipeline ---")

# 1. Load the Datasets from the data directory
# 1. Load the Datasets using the absolute path
file_path = r'D:\Home Folder\University\2026-2027\Semester8\Graduation Project II\PtM-Thermal-ML-Optimization\data\PTM_Case Study 3 Grids.xlsx'
try:
    df1 = pd.read_excel(file_path, sheet_name='Grid1', header=1).dropna(axis=1, how='all')
    df2 = pd.read_excel(file_path, sheet_name='Grid2', header=1).dropna(axis=1, how='all')
    print("Successfully loaded AVEVA simulation datasets.")
except Exception as e:
    print(f"Error loading datasets: {e}")
    exit()

# 2. Clean and Rename Columns for Feature Mapping
df1.rename(columns={
    'R1.Xrxn[1](fraction)': 'Recycle_Frac', 
    'S_022.P(bar)': 'Pressure', 
    'TotalCompWork(MW)': 'W_comp', 
    'RICH-CH4.In.z[CH4](mol frac)': 'CH4_Purity'
}, inplace=True)

df2.rename(columns={
    'HX3.Tto(°C)': 'Intercool_T', 
    'TotalCompWork(MW)': 'W_comp', 
    'TotalCoolingDuty(kW)': 'Q_C'
}, inplace=True)

# 3. Define Features (X) and Target (y) for Compressor Power Model
X = df1[['Recycle_Frac', 'Pressure']]
y = df1['W_comp']

# Split data into Training (80%) and Testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train the XGBoost Regressor Surrogate Model
model = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=4, random_state=42)
model.fit(X_train, y_train)

# 5. Evaluate Model Accuracy
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"Compressor Power Model Error (RMSE): {rmse:.4f} MW")

# 6. Run Constraints & Extract Global Optimum
valid_yields = df1[df1['CH4_Purity'] >= 0.95]
optimal_pressure_row = valid_yields.loc[valid_yields['Pressure'].idxmin()]
optimal_energy_row = df2.loc[df2['W_comp'].idxmin()]

print("\n=== MACHINE LEARNING OPTIMIZATION RESULTS ===")
print(f"Target Interstage Cooling Temp: {optimal_energy_row['Intercool_T']} °C")
print(f"Target Operating Pressure:      {optimal_pressure_row['Pressure']} bar")
print(f"Achieved Methane Purity:        {optimal_pressure_row['CH4_Purity']*100:.2f}%")
print(f"Minimized Compressor Power:     {optimal_energy_row['W_comp']:.2f} MW")
print(f"Minimized Cooling Duty:         {optimal_energy_row['Q_C']:.0f} kW")
print("===============================================\n")