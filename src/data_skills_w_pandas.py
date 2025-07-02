# Import libraries
import pandas as pd

def main():
    pass
    # Load data
    df_order = pd.read_csv('./data/input/order.csv')
    df_customer = pd.read_csv('./data/input/customer.csv')


    # Check if Nan values
    df_order.isna()

    # Count Nan values per columns
    df_order.isna().sum()

    # Get total price of all orders
    df_order["price"] = df_order['unit_price'] * df_order['quantity']
    df_order["price"].sum()

    # Remove Nan values
    df_order = df_order.dropna()

    # What is the category repartition
    df_order["category"].value_counts()

    # Standardise categories
    df_order["category"].str.title().value_counts()

    # Get .fr and .com repartition among customers
    df_customer

    # Get repartition of email provider


    # Create column full_name


    # Drop useless columns


    # Merge order and customer dataframe


    # Rename 'unit_price' to 'price' 


    # Save to output folder
