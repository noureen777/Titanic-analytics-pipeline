import pandas as pd
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import subprocess
import os

df = pd.read_csv(sys.argv[1])

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
sns.countplot(x="Survived", data=df)
plt.title("Survival Count")

if "Family_Group" in df.columns:
    plt.subplot(2,2,2)
    sns.barplot(x="Family_Group", y="Survived", data=df)
    plt.title("Survival by Family Group")

plt.subplot(2,2,3)
num = df.select_dtypes(include=['int64','float64'])
sns.heatmap(num.corr(), annot=False)
plt.title("Correlation Heatmap")

plt.tight_layout()
plt.savefig("summary_plot.png")

print("Visualization done ✅")

# 🔗 Call next script
next_script = "cluster.py"
if os.path.exists(next_script):
    subprocess.run([sys.executable, next_script, sys.argv[1]], check=True)