import sys
import pandas as pd
from sklearn.cluster import KMeans

csv_file = sys.argv[1]
df = pd.read_csv(csv_file)

pca_cols = ['PC1', 'PC2', 'PC3', 'PC4']

if all(col in df.columns for col in pca_cols):
    features = df[pca_cols]
else:
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    if 'Survived' in numeric_cols:
        numeric_cols.remove('Survived')
    features = df[numeric_cols]

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = kmeans.fit_predict(features)

counts = pd.Series(labels).value_counts().sort_index()

with open('clusters.txt', 'w') as f:
    for cluster, count in counts.items():
        f.write(f'Cluster {cluster}: {count} samples\n')

print("Clustering done ✅")