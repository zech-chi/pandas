import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    Id = 101
    return students.loc[students["student_id"] == Id, ["name", "age"]]
