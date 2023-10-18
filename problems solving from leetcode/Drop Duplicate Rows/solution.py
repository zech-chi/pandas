import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers_without_dup = customers.drop_duplicates(subset=['email'])
    return customers_without_dup
