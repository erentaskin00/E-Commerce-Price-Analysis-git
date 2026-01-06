# E-Commerce-Price-Analysis-git
Price Analysis & Anomaly Detection
This project is a Python-based data science tool that scrapes real-time price data for the iPhone 13 from e-commerce platforms, cleans the "messy" raw data, and performs statistical anomaly detection using the Interquartile 

Range (IQR) method.
As per the project requirements, here is the detailed cleaning workflow implemented in clean_price():
Standardization: All currency symbols (e.g., "TL") and hidden whitespaces are removed to prevent conversion errors.
Locale Handling: E-commerce data often uses Turkish/European formatting (dot for thousands, comma for decimals). The script identifies these patterns:
If both . and , exist (e.g., 64.999,00), dots are removed and commas are replaced with periods.
If only a comma exists, it is converted to a period.
Type Casting: Once the string is sanitized, it is converted into a float for mathematical processing.

Anomaly Detection (IQR Method)
To identify anomalies (unusually high or low prices), I utilized the Interquartile Range method:Q1 (25th Percentile): The middle number between the smallest value and the median.Q3 (75th Percentile): The middle value between the median and the highest value.IQR Calculation: $IQR = Q3 - Q1$Bounds: - Lower Bound: $Q1 - (1.5 \times IQR)$Upper Bound: $Q3 + (1.5 \times IQR)$Any price falling outside these bounds is flagged as an Is_Anomaly

The project generates two primary visualizations:
Boxplot (Seaborn): Displays the median, quartiles, and whiskers, providing a visual summary of the price distribution.
Scatterplot (Seaborn): Maps all products by index and price, highlighting detected anomalies in red for clear identification.

Installation & Usage
Clone the repository.

Install dependencies:
pip install pandas numpy beautifulsoup4 requests seaborn matplotlib

Run the script:
python aptalders.py
