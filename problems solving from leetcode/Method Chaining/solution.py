import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    more_than_100 = animals[animals['weight'] > 100]
    sortedAnimals = more_than_100.sort_values(by='weight', ascending=False)
    return sortedAnimals[['name']]
