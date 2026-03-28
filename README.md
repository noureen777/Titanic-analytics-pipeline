# Titanic Analytics Pipeline

A comprehensive end-to-end data analytics pipeline for analyzing Titanic passenger survival data using modern data science practices and containerization.

## 📋 Overview

This project implements a production-ready data analytics workflow that processes raw Titanic datasets through multiple stages of data cleaning, feature engineering, statistical analysis, visualization, and machine learning clustering. The pipeline demonstrates best practices in data science, including automated handoffs between processing stages and Docker containerization for reproducible environments.

## 🎯 Project Goals

- Extract meaningful insights from historical Titanic passenger data
- Implement robust data preprocessing and feature engineering techniques
- Perform statistical analysis and survival rate calculations
- Visualize key patterns and relationships in the data
- Apply unsupervised learning (K-Means clustering) for passenger segmentation

## 👥 Team

| Name | 
|------|
| Noureen Zafan |
| Mohamed Atef |
| Abdulrhman Ismail |
| Rokia Alaa |
| Ramez Emad |

## 📊 Pipeline Architecture

The project follows a modular, sequential pipeline architecture:

### Stage 1: Data Ingestion (`Ingest.py`)
- Loads raw Titanic dataset from CSV file

### Stage 2: Data Preprocessing (`preprocess.py`)

Implements four distinct data transformation stages:

1. **Data Cleaning**
   - Removes irrelevant columns (Cabin, Ticket, Name, PassengerId)
   - Imputes missing numeric values (Age, Fare) with median
   - Imputes missing categorical values (Embarked) with mode
   - Removes duplicate records

2. **Feature Transformation**
   - Converts gender categories (male/female → 1/0)
   - Applies one-hot encoding to embarkation ports (C, Q, S)
   - Standardizes numeric features using StandardScaler

3. **Dimensionality Reduction**
   - Combines SibSp + Parch into FamilySize feature
   - Applies PCA (Principal Component Analysis) retaining 90% variance
   - Reduces feature space while preserving information

4. **Discretization**
   - Bins Age into life stages (Child, Teen, YoungAdult, Adult, Senior)
   - Bins Fare into quartile bands (Low, Mid, High)
   - Categorizes FamilySize (Solo, Small, Large)
   - Encodes categorical bins using LabelEncoder

### Stage 3: Statistical Analytics (`analytics.py`)

Computes key survival metrics:
- Overall survival rate percentage
- Survival rates segmented by family group
- Feature variance analysis to identify most informative components

Outputs stored in:
- `insight1.txt` — Overall survival statistics
- `insight2.txt` — Family group survival breakdown
- `insight3.txt` — Highest variance feature analysis

### Stage 4: Visualization (`visualize.py`)

Generates a comprehensive visual summary with:
- Survival count distribution
- Survival rates by family group
- Feature correlation heatmap

Output: `summary_plot.png`

### Stage 5: Clustering (`cluster.py`)

Applies unsupervised learning:
- K-Means clustering (k=3) on PCA components
- Assigns passengers to 3 distinct clusters
- Outputs cluster membership counts

Output: `clusters.txt`

## 🛠️ Technology Stack

| Tool | Purpose |
|------|---------|
| **Python 3.11** | Core programming language |
| **Pandas** | Data manipulation and analysis |
| **NumPy** | Numerical computing |
| **Scikit-learn** | Machine learning and preprocessing |
| **Matplotlib & Seaborn** | Data visualization |
| **Docker** | Containerization for reproducible environments |
| **Jupyter** | Interactive notebook support |

## 📦 Installation

### Local Setup

1. Clone the repository:
```bash
git clone https://github.com/noureen777/Titanic-analytics-pipeline.git
cd Titanic-analytics-pipeline
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Docker Setup

Build and run the pipeline in a containerized environment:
```bash
docker build -t titanic-pipeline .
docker run -p 8888:8888 titanic-pipeline
```

## 🚀 Usage

### Running the Full Pipeline

Execute the entire pipeline starting from the preprocessing stage:
```bash
python preprocess.py data_raw.csv
```

The pipeline will automatically chain through all stages:
```
preprocess.py → analytics.py → visualize.py → cluster.py
```

### Running Individual Stages
```bash
# Data preprocessing
python preprocess.py data_raw.csv

# Analytics on preprocessed data
python analytics.py data_preprocessed.csv

# Visualization
python visualize.py data_preprocessed.csv

# Clustering
python cluster.py data_preprocessed.csv
```

## 📁 Project Structure
```
Titanic-analytics-pipeline/
├── preprocess.py           # Data cleaning and feature engineering
├── analytics.py            # Statistical analysis
├── visualize.py            # Visualization generation
├── cluster.py              # K-Means clustering
├── Ingest.py               # Data ingestion module
├── data_raw.csv            # Raw Titanic dataset
├── train.csv               # Training dataset
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container configuration
└── README.md               # This file
```

## 📈 Output Files

| File | Description |
|------|-------------|
| `data_preprocessed.csv` | Cleaned and transformed dataset |
| `insight1.txt` | Overall survival rate |
| `insight2.txt` | Survival rates by family group |
| `insight3.txt` | Feature variance analysis |
| `summary_plot.png` | Visualization dashboard |
| `clusters.txt` | Cluster membership distribution |

## 🔍 Key Insights

The pipeline analyzes several important dimensions:

- **Survival Demographics** — How passenger characteristics relate to survival odds
- **Family Impact** — Role of family size in survival outcomes
- **Feature Importance** — Most informative dimensions in the dataset
- **Passenger Segmentation** — Natural groupings through K-Means clustering

## 🐳 Docker Integration

The project includes a complete Docker setup for reproducible environments:
```dockerfile
FROM python:3.11-slim
# All dependencies installed automatically
```

**Build:**
```bash
docker build -t titanic-pipeline .
```

**Run:**
```bash
docker run titanic-pipeline python preprocess.py data_raw.csv
```

## 🧪 Testing

The pipeline includes data validation at each stage:

- Column existence checks before operations
- Null value handling and imputation
- Type validation and conversion
- Error handling for missing dependencies

## 📝 Notes

- PCA retains 90% of variance by default (configurable)
- K-Means uses k=3 clusters (adjust in `cluster.py` as needed)
- Missing values are handled via median/mode imputation
- Standardization applied only to numeric features
- All stages include progress indicators and confirmations

## 🔄 Pipeline Flow

The modular design allows:

- **Sequential execution** — Automatic handoff between stages
- **Standalone execution** — Run individual scripts independently
- **Containerization** — Reproducible environment across systems
- **Extensibility** — Easy to add new processing stages

## 📚 Dependencies

See `requirements.txt` for the complete list:

- **Core:** pandas, numpy, scikit-learn, scipy
- **Visualization:** matplotlib, seaborn
- **Utilities:** jupyter, nltk, textblob, requests

## 🚨 Requirements

- Python 3.11+
- 2GB RAM minimum
- 500MB disk space
- Docker (optional, for containerization)

