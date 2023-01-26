import pandas as pd

def main():
    csv_data = pd.read_csv("Assignments\Assignment2\Data\data_assignment2.csv")
    living_area = csv_data[['Living_area']]
    selling_price = csv_data[['Selling_price']]
    return living_area, selling_price
