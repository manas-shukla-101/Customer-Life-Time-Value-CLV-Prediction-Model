# Customer Life-Time Value(CLV) Prediction Model

Customer Lifetime Value(CLV) prediction using Python, RFM analysis and Random Forest Algorithm.

## Objective:

1. Predict the life-time value of customers based on their purchase behaviour to identify high-value customers.
2. Analyze the RFM (Recency, Frequency, Monetary) scores of customers to understand their purchase patterns.
3. Use Random Forest Algorithm to build a model that can predict the CLV of customers.
4. Evaluate the performance of the model using metrics such as Mean Absolute Error (MAE) and R-S quared.
5. Provide insights using graphs and tables to help business stakeholders make informed decisions.

## Use:

Python, Pandas, NumPy, Matplotlib, Scikit-learn, and Seaborn libraries are used to perform the analysis.
Excel file containing customer data is used as input.
Kaggle.com dataset is used for reference.
https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci  is used for reference.
Random Forest Algorithm is used to build the model.

## What is Random Forest Algorithm?

Random Forest Algorithm is an ensemble learning method that combines multiple decision trees to improve the accuracy and robustness of predictions. And it is used for both classification and regression tasks. Also, it is a type of supervised learning algorithm.

## Why we used Random Forest Algorithm?

Cause, it is a robust and accurate algorithm that can handle large datasets and provide good results even with noisy data. Also, it is easy to implement and interpret. And it can handle both categorical and numerical data. And it is a good choice for regression tasks. And it can handle missing values.

## How to understand the graph?

The graph shows the distribution of CLV scores for different customer segments. The x-axis represents the CLV score, and the y-axis represents the frequency of customers in each segment. The graph is divided into three segments: low CLV (0-100), medium CLV (100-500), and high CLV (500-1000). The graph shows that most customers have a low CLV, while a smaller percentage of customers have a high CLV.  This suggests that the company may need to focus on retaining and upselling to its high-value customers in this sample data.

## Project Structure:

online_retail_analysis/
│
├── main.py                 # Main execution script
├── config.py               # Configuration
├── requirements.txt        # Dependencies
├── data.csv                # Data file
├── README.md               # Documentation
├── data/
│   ├── __init__.py
│   ├── loader.py
│   └── cleaner.py
├── features/
│   ├── __init__.py
│   └── rfm.py
├── models/
│   ├── __init__.py
│   └── trainer.py
├── models/
│   ├── __init__.py
│   ├── analysis_panel.py
│   ├── data_panel.py
│   ├── main_window.py
│   └── results_panel.py
├── visualization/
│   ├── __init__.py
│   └── plots.py
└── utils/
    ├── __init__.py
    ├── helper.py
    ├── progress.py
    └── logger.py

## Installation:

requirements.txt

numpy>=1.21.0
scikit-learn>=1.0.0
tqdm>=4.0.0
python-dotenv>=0.19.0
Pillow>=9.0.0
ttkthemes>=3.2.0
matplotlib>=3.6.0
seaborn>=0.12.0
pandas>=1.5.0

## Usage:

Step 1: run main.py
Step 2: There will be option to create virtual environment and install dependencies.
Step 3: Run main.py again to start the application.
Step 4: If you want to use your own data, replace data.csv with your data file.
Step 5: Run main.py again to start the application.
Step 6: Now select the option to load data from csv file.
Step 7: If you want to view the data, select the option to view data.
Step 8: If you want to perform analysis, select the option to perform analysis.
Step 9: In analysis panel, select the option to perform RFM analysis.
Step 10: In RFM analysis panel, select the option to view RFM scores.
Step 11: Now click train model button to train the model.
Step 12: To see result, click on the result button.
Step 13: Now you can view the result in the result panel.
Step 14: To save the result, click on the save button.

## Output:

Outputs will be saved in the `output/` directory which will be created in the root directory automatically. The output will be in the form of a CSV file named `output.csv`. The CSV file will contain the RFM scores, the predicted values and average order value.