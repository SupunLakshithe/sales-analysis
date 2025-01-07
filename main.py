import data_proc

def choose_data_processing_strategy():
    print("\nChoose Data Processing Strategy")
    print("\t1. Monthly Sales Analysis")
    print("\t2. Price Analysis")
    print("\t3. Weekly Sales Analysis")
    print("\t4. Product Preference Analysis")
    print("\t5. Total Purchases Analysis")

    choice = (input("Enter your choice (1-5): "))
    return choice


def choose_output_strategy():
    print("Choose Output Strategy:")
    print("1. Text Report")
    print("2. CSV Report")
    print("3. Row data Report")
    print("4. HTML web Report")

    choice = (input("Enter your choice (1-4): "))
    return choice


def main(data):
    data_processing_strategy = choose_data_processing_strategy()
    output_strategy = choose_output_strategy()
    if (data_processing_strategy == '1'):
        data_processing_contex.set_strategy(month_sales)
    elif (data_processing_strategy == '2'):
        data_processing_contex.set_strategy(price_analysis)
    elif(data_processing_strategy == '3'):
        data_processing_contex.set_strategy(week_analysis)
    elif(data_processing_strategy == '4'):
        data_processing_contex.set_strategy(product_analysis)
    elif(data_processing_strategy == '5'):
        data_processing_contex.set_strategy(distribution_of_sales_analysis)
    else:
        print("Error! Invalid choice for Data Processing Strategy")
        exit(0)

    if (output_strategy=='1'):
        data_report_context.set_strategy(text_report)
    elif(output_strategy=='2'):
        data_report_context.set_strategy(csv_report)
    elif(output_strategy=='3'):
        data_report_context.set_strategy(raw_report)
    elif (output_strategy == '4'):
        data_report_context.set_strategy(html_report)
    else:
        print("Error! Invalid choice for Data Reporting Strategy")
        exit(0)

    print("\nSelected Data Processing Strategy:", data_processing_strategy)
    print("Selected Output Strategy:", output_strategy)

    process_data=data_processing_contex.excute_strategy(data)
    data_report_context.generate_report(process_data)

    # Perform processing and output based on choices


if __name__ == "__main__":

    file = 'C:\\Users\slsom\\all_data_with_week.json'

    json_data = data_proc.JSONDataIngestion()
    data_ingestion_context = data_proc.DataIngestionContext()

    data_ingestion_context.set_strategy(json_data)

    # get data <-------------------------------------data
    data = data_ingestion_context.ingest_data(file)

    month_sales = data_proc.MonthlySalesAnalysis()
    price_analysis = data_proc.PriceAnalysis()
    week_analysis = data_proc.WeeklySalesAnalysis()
    product_analysis = data_proc.ProductPreferenceAnalysis()
    distribution_of_sales_analysis = data_proc.TotalPerchasesAnalysis()
    data_processing_contex = data_proc.DataProcessingContex()

    text_report = data_proc.TextReportStrategy()
    csv_report = data_proc.CSVReportStrategy()
    raw_report = data_proc.ReturnReportstrategy()
    html_report = data_proc.HTMLReportstratergy()
    data_report_context = data_proc.DataReportingContext()

    while True:
        main(data)
        exit_choice = input("\nEnter 0 to exit or any other to continue: ")
        if exit_choice == "0":
            break

