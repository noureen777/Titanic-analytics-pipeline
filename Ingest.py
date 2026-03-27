import sys
import subprocess
import pandas as pd

if len(sys.argv) < 2:
    print("Please provide a file name (example: python ingest.py train.csv)")
    sys.exit()

df = pd.read_csv(sys.argv[1])
df.to_csv("data_raw.csv", index=False)
print("data_raw.csv created")

print("Starting preprocessing...")

subprocess.run([sys.executable, "preprocess.py", "data_raw.csv"], check=True)