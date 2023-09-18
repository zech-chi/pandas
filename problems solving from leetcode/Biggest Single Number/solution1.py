import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    dic = {}
    for n in my_numbers.num:
        if n in dic:
            dic[n] += 1
        else:
            dic[n] = 1
    
    single_numbers = []
    for n in dic:
        if dic[n] == 1:
            single_numbers.append(n)
    if len(single_numbers) == 0:
        return pd.DataFrame({"num": [None]})
    return pd.DataFrame({"num": [max(single_numbers)]})
        
