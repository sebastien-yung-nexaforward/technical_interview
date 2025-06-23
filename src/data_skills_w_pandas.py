# Import libraries
import pandas as pd
import os

def main():
    # Load data
    path_customers = os.path.join("data", "input", "customer.csv")
    path_order = os.path.join("data", "input", "order.csv")
    
    customers = pd.read_csv(path_customers)
    orders = pd.read_csv(path_order)

    # Check if Nan values


    # Count Nan values per columns
    ordersna = orders.isna()
    for column in ordersna.columns:
        ordersna[column].sum()

    # Get total price of all orders
    orders.apply(lambda x: x["quantity"] * x["unit_price"], axis=1).sum()

    # Remove Nan values
    orders.dropna(inplace=True, axis=1)

    # What is the category repartition
    

    # Standardise categories
    orders["category"] = orders["category"].str.title()

    # Get .fr and .com repartition among customers


    # Get repartition of email provider


    # Create column full_name


    # Drop useless columns


    # Merge order and customer dataframe


    # Rename 'unit_price' to 'price' 


    # Save to output folder
