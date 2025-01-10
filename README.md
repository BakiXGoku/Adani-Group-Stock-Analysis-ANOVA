# ANOVA Analysis of Stock Prices

## Overview
This project performs an Analysis of Variance (ANOVA) on three stocks to compare their means and identify statistically significant differences. A violin plot is used as a visualization to represent the distribution of the data.

## Stock Descriptions and Background
The stocks analyzed in this project are:

- **ADANIGREEN**: Adani Green Energy Limited operates in the renewable energy sector, focusing on solar and wind power generation. It is a leading player in India's renewable energy market and is committed to sustainability and clean energy solutions.

- **ATGL**: Adani Total Gas Limited is a major player in the natural gas sector. The company focuses on city gas distribution, providing clean and efficient energy solutions to industrial, commercial, and residential customers across India.

- **ADANIENSOL**: Adani Energy Solutions Limited specializes in power transmission and distribution. The company plays a critical role in India's energy infrastructure by ensuring the reliable delivery of electricity across the country.

## Project Structure
- **Data**: Raw stock data for analysis is stored in CSV files.
- **Scripts**: Python scripts to run the ANOVA analysis and generate visualizations.
- **Results**: Output files, including ANOVA results and violin plot images.

## Significance of the Project
ANOVA is a powerful statistical tool to analyze and compare the means of multiple groups. In this project, ANOVA is applied to stock data, making it useful for stock market enthusiasts to evaluate patterns in stock performance over time.

The violin plot provides a clear visual comparison of the data distributions for each stock, helping to uncover insights beyond mean differences.

## Files and Folders
### data/
Contains raw CSV files of stock data:
- `ADANIENSOL.csv`
- `ADANIGREEN.csv`
- `ATGL.csv`

### scripts/
Python scripts for analysis and visualization:
- `anova_analysis.py`

### results/
Stores output files:
- `anova_results.txt`
- `violin_plot.png`


### Other Files
- `README.md`: Project documentation (this file).
- `requirements.txt`: Dependencies required to run the scripts.

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project_directory>
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the analysis script:
   ```bash
   python scripts/anova_analysis.py
   ```
5. Generate the violin plot:
   ```bash
   python scripts/violin_plot.py
   ```

## Results
- The ANOVA results, including the F-statistic and p-value, are stored in `results/anova_results.txt`.
- The violin plot comparing the stock distributions is saved as `results/violin_plot.png`.

## Contribution
Contributions are welcome! Feel free to fork the repository, create a branch, and submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
