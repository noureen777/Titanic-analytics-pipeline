import pandas as pd
import sys
import subprocess
import os

df = pd.read_csv(sys.argv[1])

# Insight 1
survival_rate = df["Survived"].mean()
with open("insight1.txt", "w") as f:
    f.write(f"Survival rate is {survival_rate*100:.2f}% of passengers.")

# Insight 2
if "Family_Group" in df.columns:
    group_survival = df.groupby("Family_Group")["Survived"].mean()
    with open("insight2.txt", "w") as f:
        f.write("Survival rate by family group:\n")
        f.write(group_survival.to_string())

# Insight 3
pca_cols = [col for col in df.columns if "PC" in col]
if pca_cols:
    variances = df[pca_cols].var()
    top_pc = variances.idxmax()
    with open("insight3.txt", "w") as f:
        f.write(f"The feature with highest variance is {top_pc}.")

print("Analytics done ✅")

# 🔗 Call next script
next_script = "visualize.py"
if os.path.exists(next_script):
    subprocess.run([sys.executable, next_script, sys.argv[1]], check=True)