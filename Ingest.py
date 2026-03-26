import sys
import pandas as pd
import subprocess
if len(sys.argv) < 2:
    print("Please provide a file name (example: python Ingest.py train.csv)")
    sys.exit()
df = pd.read_csv(sys.argv[1])
df.to_csv("data_raw.csv", index=False)
print("data_raw.csv created")
subprocess.run(["python", "preprocess.py", "data_raw.csv"])