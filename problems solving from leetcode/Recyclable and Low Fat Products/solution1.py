import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    arr = []
    for i in range(len(products)):
        if products.low_fats[i] == 'Y' and products.recyclable[i] == 'Y':
            arr.append(products.product_id[i])
    res = pd.DataFrame({"product_id": arr})
    return res
