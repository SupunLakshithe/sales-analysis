import json
import pandas as pd
import matplotlib.pyplot as plt
import webbrowser
from abc import ABC ,abstractmethod

### Strategy Pattern: Data Processing Strategies ###


## Interface
class DataProcess(ABC):
    @abstractmethod
    def process_data(self ,data):
        pass


## Concrete class
class MonthlySalesAnalysis(DataProcess):
    def process_data(self ,data):
        pd_data = panda_data_frame(data)
        #Convert the 'date' column to datetime format for easier manipulation
        pd_data['date'] = pd.to_datetime(pd_data['date'])
        # Group the data by 'branch_id' and 'year_month' and calculate the total sales
        pd_data['year_month'] = pd_data['date'].dt.to_period('M')
        #analyse data
        pd_data_quantity=(pd_data.groupby(['branch_id', 'year_month']).agg({'quantity': 'sum', 'price': 'sum'})
                          .sort_values(by='quantity', ascending=False).reset_index())
        pd_data_quantity.rename(columns={'price':'Total_income'},inplace=True)
        print("monthly data analysing ...")
        return pd_data_quantity

class PriceAnalysis(DataProcess):
    def process_data(self ,data):
        pd_data = panda_data_frame(data)
        product_analysis = pd_data.groupby('product_id').agg({
            'quantity': ['sum', 'mean'],  # Total quantity sold and average quantity per transaction
            'price': lambda x: x.iloc[0],  # Price of one item (assuming price is constant for a product)
            'transaction_id': 'count'  # Count of transactions for each product
        }).reset_index()
        #rename columns
        product_analysis.columns = ['Product_id', 'Total_quantity_sold', 'Average_quantity_per_transaction',
                                    'Price_of_one_item', 'Transaction_count']
        #sorting base on quantity
        product_analysis = product_analysis.sort_values(by='Total_quantity_sold',ascending=False).reset_index()
        print("price analysing ...")
        return product_analysis

class WeeklySalesAnalysis(DataProcess):
    def process_data(self ,data):
        pd_data = panda_data_frame(data)
        weekly_sales = pd_data.groupby(['week_number', 'branch_id']).agg({'quantity': 'sum', 'price': 'sum'})
        #sorting base on week number and quantity
        weekly_sales = weekly_sales.sort_values(by=['week_number', 'quantity'], ascending=[True, False]).reset_index()
        #rename columns
        weekly_sales.columns = ['Week_number', 'Branch_id', 'Quantity_of_items_sold', 'Income']
        print("Weekly data analysing ...")
        return weekly_sales

class ProductPreferenceAnalysis(DataProcess):
    def process_data(self ,data):
        pd_data = panda_data_frame(data)
        product_preference = pd_data.groupby('product_id').agg({
            'quantity': 'sum',
            'price': ['mean','sum'],  # average price
            'transaction_id': 'count'  # number of transactions
        })
        #rename
        product_preference.columns=['Total_Quantity_Sold','Average_income','Total_income','Number_of_Transactions']
        # sorting base on quantity
        product_preference = product_preference.sort_values(by='Total_Quantity_Sold', ascending=False).reset_index()
        print("Product Preference data analysing ...")
        return product_preference

class TotalPerchasesAnalysis(DataProcess):
    def process_data(self ,data):
        pd_data = panda_data_frame(data)
        pd_data['total_sales_amount'] = pd_data['quantity'] * pd_data['price']
        weekly_sales = pd_data.groupby('week_number').agg({'total_sales_amount': 'sum'}).reset_index()
        branch_sales = pd_data.groupby('branch_id').agg({'total_sales_amount': 'sum'}).reset_index()

        #plotting
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))
        # Plot weekly sales
        weekly_sales.plot(kind='bar', color='skyblue', ax=ax1)
        ax1.set_title('Distribution of Total Sales Amount by Week')
        ax1.set_xlabel('Week Number')
        ax1.set_ylabel('Total Sales Amount')
        # Plot branch sales
        branch_sales.plot(kind='bar', color='skyblue', ax=ax2)
        ax2.set_title('Distribution of Total Sales Amount by Branch')
        ax2.set_xlabel('Branch ID')
        ax2.set_ylabel('Total Sales Amount')
        # Adjust layout
        plt.tight_layout()
        # Show the plot
        plt.show()

        branch_sales.columns=['Branch_id','Total_income']
        print("anlysing total sales")
        return branch_sales


## Context
class DataProcessingContex:
    def __init__(self):
        pass

    def excute_strategy(self ,data):
        data = self.strategy.process_data(data)
        #convert to dictionary
        data = data.to_dict(orient='records')
        return data

    def set_strategy(self ,strategy):
        self.strategy =strategy

# Helper methode
def panda_data_frame(data):
    pd_data = pd.DataFrame(data['sales_data'])
    return pd_data







### Strategy Pattern: Data Ingestion Strategies ###

## interface
class DataIngestionStrategy(ABC):
    @abstractmethod
    def ingest_data(self, file_path):
        pass


## concrete class
class JSONDataIngestion(DataIngestionStrategy):
    def ingest_data(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data


## Context
class DataIngestionContext:
    def __init__(self):
        pass

    def set_strategy(self, strategy):
        self.strategy = strategy

    def ingest_data(self, file_path):
        return self.strategy.ingest_data(file_path)







### Strategy Pattern: Data Reporting Strategies ###

## interface
class DataReportingStrategy(ABC):
    @abstractmethod
    def generate_report(self, data):
        pass


## concrete class
class TextReportStrategy(DataReportingStrategy):
    def generate_report(self, data):
        data_frame = pd.DataFrame(data)
        #pd.set_option('display.max_columns', None) # <-- comment if columns fckedup
        report = f"Text Report:\n{data_frame}\n\nDescribe Analys:\n{data_frame.describe()}"
        print(report)
        return report

class CSVReportStrategy(DataReportingStrategy):
    def generate_report(self, data):
        # Assume data is a list of dictionaries
        header = ','.join(data[0].keys())
        rows = '\n'.join([','.join(map(str, row.values())) for row in data])
        report = f"CSV Report:\n{header}\n{rows}"
        with open("report.csv","w") as csv_file:
            csv_file.write(f"{header}\n{rows}")
        print(report)
        return report

class ReturnReportstrategy(DataReportingStrategy):
    def generate_report(self, data):
        print(data)

class HTMLReportstratergy(DataReportingStrategy):
    def generate_report(self, data):
        data_frame = pd.DataFrame(data)
        report_html = f"<h1>Text Report:</h1>\n{data_frame.to_html()}\n\n<h1>Describe Analysis:</h1>\n{data_frame.describe().to_html()}"

        # Save the HTML report to a file
        with open("report.html", "w") as html_file:
            html_file.write(report_html)
        webbrowser.open("report.html")
        print("HTML report generated successfully.")
        return report_html


## Context
class DataReportingContext:
    def __init__(self):
        pass

    def set_strategy(self, strategy):
        self.strategy = strategy

    def generate_report(self, data):
        return self.strategy.generate_report(data)