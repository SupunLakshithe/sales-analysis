# Sales Analysis Project

This project provides a comprehensive analysis of sales data using the **Strategy Pattern** for modularity and flexibility. It supports multiple strategies for data ingestion, processing, and reporting.

---

## Features

- **Data Processing**: Analyze sales data by applying various strategies.
  - Monthly Sales Analysis
  - Price Analysis
  - Weekly Sales Analysis
  - Product Preference Analysis
  - Total Purchases Analysis
- **Data Reporting**: Generate reports in different formats.
  - Text Report
  - CSV Report
  - Raw Data Output
  - HTML Web Report

---

## Project Structure

- **main.py**: Entry point of the application. Handles user interaction and executes the selected strategies.
- **data_proc.py**: Contains strategy implementations for data processing, ingestion, and reporting.
- **all_data_with_week.json**: Input sales data in JSON format.

---

## Setup and Usage

### Prerequisites

- Python 3.7+
- Required Python libraries:
  - `pandas`
  - `matplotlib`
  - `json`

Install the dependencies using:

```bash
pip install pandas matplotlib
```
### Installation Steps
#### Clone the Repository:

```bash
git clone https://github.com/SupunLakshithe/sales-analysis.git
cd sales-analysis
```
## Verify Files:
Ensure the following files are in the project directory:

- `main.py`
- `data_proc.py`
- `all_data_with_week.json`

## Run the Application:

```bash
python main.py
```

# Running the Application
Upon starting the application, follow the on-screen prompts:

## Choose Data Processing Strategy:
1. Monthly Sales Analysis
2. Price Analysis
3. Weekly Sales Analysis
4. Product Preference Analysis
5. Total Purchases Analysis

## Choose Output Strategy:
1. Text Report
2. CSV Report
3. Raw Data Report
4. HTML Web Report

### Example Command Workflow:
1. Start the application: `python main.py`.
2. Choose an option for data processing (e.g., `1` for Monthly Sales Analysis).
3. Choose an output option (e.g., `4` for HTML Web Report).
4. Follow the instructions to view the generated output.

![image](https://github.com/user-attachments/assets/c899d681-bd39-417f-b668-97c565fbf058)

---

# Example Output

- **Text Report**: Displays detailed statistics in the terminal.
![image](https://github.com/user-attachments/assets/83ac7986-14f8-417c-8590-7dfb688a5b2f)

- **CSV Report**: Saves the analysis results to `report.csv`.
![image](https://github.com/user-attachments/assets/627a51df-cb79-4153-9838-1458c5512323)

- **HTML Report**: Generates an HTML file (`report.html`) and opens it in your default web browser.
- **Raw Data Report**: Prints the raw processed data to the console.

---

# Example Data Format
The input data (`all_data_with_week.json`) contains:

- `transaction_id`: Unique identifier for each transaction.
- `branch_id`: Identifier for the branch.
- `product_id`: Identifier for the product.
- `quantity`: Quantity sold.
- `price`: Price of the product.
- `date`: Date of the transaction.
- `week_number`: Week number of the year.

---

# Project Flow

## Data Ingestion
- **JSONDataIngestion**: Loads JSON data from the provided file.

## Data Processing
Strategies include:
- **MonthlySalesAnalysis**: Summarizes sales per branch by month.
- **PriceAnalysis**: Analyzes product-level pricing and quantity trends.
- **WeeklySalesAnalysis**: Shows weekly sales trends by branch.
- **ProductPreferenceAnalysis**: Displays most sold products and their income contributions.
- **TotalPurchasesAnalysis**: Computes total sales amounts.

## Data Reporting
- **TextReportStrategy**: Outputs analysis results as a text summary.
- **CSVReportStrategy**: Saves results as a CSV file.
- **HTMLReportStrategy**: Generates and opens an HTML report.
- **ReturnReportStrategy**: Prints raw data in dictionary format.

---

# License
This project is licensed under the MIT License. See `LICENSE` for more details.

---

# Contact
For questions or suggestions, feel free to reach out:

- GitHub: SupunLakshithe
- Email: slsomarathna47@gmail.com
