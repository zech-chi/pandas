import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    products.set_index('product_id', inplace=True)
    products = products.stack(dropna=True).reset_index()
    products.columns = ['product_id', 'store', 'price']
    return products
