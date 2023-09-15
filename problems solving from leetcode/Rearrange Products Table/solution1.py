import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    res = pd.DataFrame(columns = ["product_id", "store", "price"])

    for i in range(len(products)):
        Id = products.product_id[i]
        price1 = products.store1[i]
        price2 = products.store2[i]
        price3 = products.store3[i]

        if not pd.isna(price1):
            res = res._append({"product_id": Id, "store": "store1", "price": price1}, ignore_index=True)
        if not pd.isna(price2):
            res = res._append({"product_id": Id, "store": "store2", "price": price2}, ignore_index=True)
        if not pd.isna(price3):
            res = res._append({"product_id": Id, "store": "store3", "price": price3}, ignore_index=True)
    
    return res
