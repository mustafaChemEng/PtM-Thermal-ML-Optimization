import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the dataset (update path if necessary)
file_path = r'd:\Home Folder\University\2026-2027\Semester8\Graduation Project II\PtM-Thermal-ML-Optimization\data\PTM_Case Study 3 Grids.xlsx'

df1 = pd.read_excel(file_path, sheet_name='Grid1', header=1).dropna(axis=1, how='all')

# 2. Rename columns for clean correlation mapping
df1.rename(columns={
    'R1.Xrxn[1](fraction)': 'Recycle_Frac', 
    'S_022.P(bar)': 'Pressure', 
    'TotalCompWork(MW)': 'W_comp', 
    'RICH-CH4.In.z[CH4](mol frac)': 'CH4_Purity'
}, inplace=True)

# Select numerical columns of interest
corr_df = df1[['Recycle_Frac', 'Pressure', 'W_comp', 'CH4_Purity']].corr()

# 3. Generate the Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_df, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Process Parameter Correlations (PtM Plant Optimization)', fontsize=12, fontweight='bold')

# 4. Save directly to the docs folder
output_path = r'd:\Home Folder\University\2026-2027\Semester8\Graduation Project II\PtM-Thermal-ML-Optimization\docs\correlations.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')

print(f"Heatmap successfully generated and saved to: {output_path}")