# Import libraries
import pandas as pd
import os

def main() -> None:
    """
    Ceci est une docstring
    
    Output: None
    """
    # Load data
    path_customers = os.path.join("data", "input", "customer.csv")
    path_orders = os.path.join("data", "input", "order.csv")
    customers = pd.read_csv(path_customers)
    orders = pd.read_csv(path_orders)

    # Check if Nan values
    print("Any missing values in customers?\n", customers.isna().any())
    print("Any missing values in orders?\n", orders.isna().any())

    # Count Nan values per columns
    print("Missing values per column in customers:\n", customers.isna().sum())
    print("Missing values per column in orders:\n", orders.isna().sum())

    # Remove Nan values
    customers_clean = customers.dropna(axis=0)
    orders_clean = orders.dropna(axis=0)
    print("Shape after dropping NaNs - customers:", customers_clean.shape)
    print("Shape after dropping NaNs - orders:", orders_clean.shape)

    # What is the category repartition
    print("Category distribution before standardization:\n", orders_clean['category'].value_counts())

    # Standardise categories
    orders_clean['category'] = orders_clean['category'].str.strip().str.title()
    print("Category distribution after standardization:\n", orders_clean['category'].value_counts())

    # Get .fr and .com repartition among customers
    customers_clean['email_domain'] = customers_clean['email'].str.split('.').str[-1]
    domain_counts = customers_clean['email_domain'].value_counts()
    print(".fr vs .com domain distribution:\n", domain_counts)

    # Get repartition of email provider
    customers_clean['email_provider'] = customers_clean['email'].str.split('@').str[-1].str.split('.').str[0]
    provider_counts = customers_clean['email_provider'].value_counts()
    print(".fr vs .com domain distribution:\n", domain_counts)

    # Create column full_name
    customers_clean['full_name'] = customers_clean['first_name'] + ' ' + customers_clean['last_name'].str.upper()
    print("Sample full_name column:\n", customers_clean[['first_name','last_name','full_name']].head())

    # Drop Firstname, Lastname, Email provider, Email domain
    customers_clean = customers_clean.drop(columns=['first_name', 'last_name', 'email_domain', 'email_provider'])
    print("Columns after dropping columns:\n", customers_clean.columns)

    # Merge order and customer dataframe
    merged = pd.merge(orders_clean, customers_clean, on='customer_id', how='inner')
    print("Merged DataFrame shape:", merged.shape)
    print("Merged sample data:\n", merged.head())

    # Save to output folder
    path_output = os.path.join("data", "output")
    os.makedirs(path_output, exist_ok=True)
    path_result_output = os.path.join(path_output, "result.csv")
    merged.to_csv(path_result_output, index=False)
    print("Merged data saved to output/merged.csv")
    return merged
