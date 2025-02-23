# Sectoral Influence vs. Parent Company Impact: A Study of Adani Group Stocks

## Table of Contents
- [Overview](#overview)
- [Stock Descriptions and Background](#stock-descriptions-and-background)
- [Project Structure](#project-structure)
- [Significance of the Project](#significance-of-the-project)
- [Methodologies Explained](#methodologies-explained)
- [Files and Folders](#files-and-folders)
- [How to Run the Project](#how-to-run-the-project)
- [Results](#results)
- [Contribution](#contribution)
- [License](#license)

## Overview
This project conducts a comprehensive statistical and econometric analysis of three Adani Group stocks. It uses Analysis of Variance (ANOVA) to compare means, a GARCH model to analyze volatility, and Value at Risk (VaR) and Conditional Value at Risk (CVaR) to assess risk. Visualizations, including a violin plot, are generated to represent data distributions and model outputs.

## Stock Descriptions and Background
The stocks analyzed in this project are:

- **ADANIGREEN**: Adani Green Energy Limited operates in the renewable energy sector, focusing on solar and wind power generation. It is a leading player in India's renewable energy market and is committed to sustainability and clean energy solutions.
- **ATGL**: Adani Total Gas Limited is a major player in the natural gas sector. The company focuses on city gas distribution, providing clean and efficient energy solutions to industrial, commercial, and residential customers across India.
- **ADANIENSOL**: Adani Energy Solutions Limited specializes in power transmission and distribution. The company plays a critical role in India's energy infrastructure by ensuring the reliable delivery of electricity across the country.

## Project Structure
```
ANOVA-ANALYSIS/
├── Results/          # Folder for output files, including statistical results and visualizations
├── Scripts/          # Folder for Python scripts and Jupyter notebooks used in the analysis
└── README.md         # Project documentation
```

## Significance of the Project
This project leverages advanced statistical and financial modeling techniques to provide insights into stock performance and risk:

- **ANOVA**: Compares the means of stock returns to identify statistically significant differences.
- **GARCH Model**: Models and forecasts stock price volatility, capturing time-varying volatility patterns.
- **VaR and CVaR**: Quantify potential losses and tail risk under normal and extreme market conditions, aiding risk management.
- **Violin Plot**: Visualizes the distribution of stock returns for intuitive insights.

These tools are valuable for stock market enthusiasts, financial analysts, and researchers studying volatility, risk, and performance patterns in the Adani Group stocks.

## Methodologies Explained

### **ANOVA (Analysis of Variance)**
A statistical method used to compare the means of three or more groups to determine if there are significant differences. In this project, ANOVA tests whether the mean returns of ADANIGREEN, ATGL, and ADANIENSOL differ significantly, helping identify performance variations across stocks.

### **GARCH (Generalized Autoregressive Conditional Heteroskedasticity)**
A time-series model used to analyze and forecast volatility in financial data. GARCH captures the clustering of volatility (periods of high volatility followed by high volatility, and low by low) and is particularly useful for modeling stock price fluctuations, providing insights into risk and uncertainty.

### **VaR (Value at Risk)**
A risk measure that estimates the potential loss in value of a portfolio over a defined time period for a given confidence level (e.g., 95%). It indicates the maximum expected loss under normal market conditions, making it a key tool for risk assessment.

### **CVaR (Conditional Value at Risk)**
Also known as Expected Shortfall, CVaR measures the expected loss in the worst-case scenarios beyond the VaR threshold. It provides a more comprehensive view of tail risk, capturing the average loss in the (1-confidence level)% tail of the distribution.

## Files and Folders
### **ANOVA-ANALYSIS/**
Contains the main project files and subdirectories.

### **Results/**
Stores output files:
- `anova_results.txt`: ANOVA F-statistic and p-value.
- `results.html`: HTML report summarizing analysis results.
- `violin_plot.png`: Violin plot of stock return distributions.

### **Scripts/**
Contains analysis and visualization scripts:
- `analysis.ipynb`: Jupyter notebook for interactive analysis.
- `anova_analysis.py`: Python script for ANOVA analysis.

### **Other Files**
- `.gitattributes`: Git configuration file.
- `.gitignore`: Specifies files to ignore in version control.
- `LICENSE`: Project license file.
- `README.md`: Project documentation (this file).
- `README.md.txt`: Duplicate or alternate README file (optional).
- `requirements.txt`: Dependencies required to run the scripts.

## How to Run the Project

### Clone the repository:
```bash
git clone <repository_url>
```

### Navigate to the project directory:
```bash
cd ANOVA-ANALYSIS
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

### Run the Python script:
```bash
python Scripts/anova_analysis.py
```

### Open the Jupyter notebook for interactive analysis:
```bash
jupyter notebook Scripts/analysis.ipynb
```

## Results
- **ANOVA**: Results (F-statistic and p-value) are saved in `Results/anova_results.txt`.
- **Visualizations**: The violin plot is saved as `Results/violin_plot.png`, with additional results summarized in `Results/results.html`.

## Contribution
Contributions are welcome! Feel free to fork the repository, create a branch, and submit a pull request with enhancements or bug fixes.

## License
This project is licensed under the MIT License.


