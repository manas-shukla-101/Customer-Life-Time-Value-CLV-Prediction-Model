# 📊 Customer Lifetime Value (CLV) Prediction Model

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-green)
![Pandas](https://img.shields.io/badge/Data%20Analysis-Pandas-yellow?logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange?logo=scikitlearn)
![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-blue)
![Seaborn](https://img.shields.io/badge/Visualization-Seaborn-purple)
![Status](https://img.shields.io/badge/Project-Completed-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

# 📌 Overview

Customer Lifetime Value (**CLV**) is a key business metric that helps companies understand how valuable a customer is over the entire duration of their relationship.

This project builds a **Machine Learning model to predict Customer Lifetime Value using RFM analysis and Random Forest Regression**.

The system analyzes customer purchasing behavior and predicts which customers are **high-value**, allowing businesses to make **data-driven marketing and retention decisions**.

---

## 📑 Table of Contents

| Section | Description |
|---------|-------------|
| [📌 Overview](#-overview) | Project introduction & CLV definition |
| [🚀 Key Features](#-key-features) | Core capabilities and functionality |
| [🎯 Problem Statement](#-problem-statement) | Challenges in customer value identification |
| [💡 Solution](#-solution) | The RFM & Random Forest approach |
| [📊 RFM Analysis](#-rfm-analysis) | Breakdown of Recency, Frequency, and Monetary metrics |
| [🤖 ML Model](#-machine-learning-model) | Random Forest Regression details |
| [📈 Model Evaluation](#-model-evaluation) | Metrics (MAE and R² Score) |
| [📊 Visualizations](#-visualizations) | Insights on customer behavior |
| [🗂 Project Structure](#-project-structure) | Repository organization |
| [⚙️ Installation](#️-installation) | Step-by-step setup guide |
| [▶️ Usage](#️-usage) | How to run the application |
| [📂 Output](#-output) | Data export details |
| [📚 Dataset](#-dataset) | Source of retail transactions |
| [🛠 Tech Stack](#-tech-stack) | Tools and libraries used |
| [📌 Future Improvements](#-future-improvements) | Roadmap for development |
| [🌐 Socials](#-socials) | Contact and portfolio |

---

# 🚀 Key Features

✔ Customer segmentation using **RFM Analysis**  
✔ Machine Learning model for **CLV prediction**  
✔ Interactive **analysis panels**  
✔ Automatic **data cleaning pipeline**  
✔ Visualization of **customer behavior patterns**  
✔ Export results to **CSV reports**  
✔ Modular and scalable **Python architecture**

---

# 🎯 Problem Statement

Businesses often struggle to identify:

- Which customers generate the **most long-term value**
- Which customers are likely to **churn**
- Where to focus **marketing and retention efforts**

Without predictive insights, companies may spend resources inefficiently.

---

# 💡 Solution

This project solves the problem by:

1. Performing **RFM Analysis**
2. Engineering customer behavior features
3. Training a **Random Forest Regression Model**
4. Predicting **Customer Lifetime Value**
5. Providing visual insights for **business decisions**

---

# 📊 RFM Analysis

RFM stands for:

| Metric | Meaning |
|------|------|
| **Recency** | How recently a customer purchased |
| **Frequency** | How often a customer purchases |
| **Monetary** | How much money a customer spends |

Using these metrics, customers can be segmented into groups such as:

- High Value Customers
- Loyal Customers
- At Risk Customers
- Low Value Customers

---

# 🤖 Machine Learning Model

### Algorithm Used
**Random Forest Regression**

Random Forest is an **ensemble learning algorithm** that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

### Why Random Forest?

✔ Handles large datasets efficiently  
✔ Works well with **non-linear relationships**  
✔ Robust to noisy data  
✔ Reduces overfitting  
✔ Provides high prediction accuracy

---

# 📈 Model Evaluation

The model performance is evaluated using:

- **Mean Absolute Error (MAE)**
- **R² Score**

These metrics measure how close the predicted CLV values are to the actual values.

---

# 📊 Visualizations

The project generates graphs to help understand customer behavior:

- CLV distribution
- Customer segmentation
- RFM score visualization
- Purchase patterns

Example insight:

> Most customers fall into the **low CLV segment**, while a small percentage contribute significantly to revenue.

This insight helps businesses focus on **retention and upselling strategies**.

---

## 🗂 Project Structure
```text
online_retail_analysis/
│
├── main.py                 # Main execution script  
├── config.py               # Configuration settings  
├── requirements.txt        # Dependencies  
├── data.csv                # Input dataset  
├── README.md               # Documentation  
│
├── data/                   # Data processing modules  
│   ├── __init__.py  
│   ├── loader.py           # Data loading utilities  
│   └── cleaner.py          # Data cleaning functions  
│
├── features/               # Feature engineering  
│   ├── __init__.py  
│   └── rfm.py              # RFM feature generation  
│
├── models/                 # Machine learning models  
│   ├── __init__.py  
│   └── trainer.py          # Model training logic  
│
├── ui/                     # Application interface  
│   ├── __init__.py  
│   ├── analysis_panel.py  
│   ├── data_panel.py  
│   ├── main_window.py  
│   └── results_panel.py  
│
├── visualization/          # Graphs and charts  
│   ├── __init__.py  
│   └── plots.py  
│
└── utils/                  # Helper utilities  
    ├── __init__.py  
    ├── helper.py  
    ├── progress.py  
    └── logger.py
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/manas-shukla-101/Customer-Life-Time-Value-CLV-Prediction-Model.git 
cd CLV-Prediction
```

### 2️⃣ Create a virtual environment
```bash
python -m venv venv
```

### Activate environment
```bash
# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage
Run the main application:
```bash
python main.py
```

### Workflow

1. Load dataset (CSV)
2. View dataset summary
3. Perform **RFM analysis**
4. Train **Random Forest model**
5. Visualize results
6. Export prediction output

---

## 📂 Output

The application automatically creates an **output directory**.

Example:

output/
└── output.csv


The file includes:

- Customer ID
- RFM Scores
- Predicted CLV
- Average Order Value

---

## 📚 Dataset

Dataset used for reference:

https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci

The dataset contains **real-world online retail transactions** used for CLV prediction.

---

## 🛠 Tech Stack

**Programming Language**

- Python

**Libraries**

- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- TQDM
- Pillow
- TTKThemes

---

## 📌 Future Improvements

- Deploy as a **web application**
- Integrate with **Power BI**
- Add **REST API for predictions**
- Implement **Deep Learning models**
- Add **customer churn prediction**

---
---
**Made with ❤️ by Manas Shukla**

---

## 🌐 Socials:
[![Portfolio](https://img.shields.io/badge/Portfolio-Website-blue)](https://manas-shukla-portfolio.framer.website) [![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://instagram.com/manas_shukla_101) [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/manas-shukla-006774370) [![email](https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white)](mailto:shuklamanas8928@gmail.com) 

---
