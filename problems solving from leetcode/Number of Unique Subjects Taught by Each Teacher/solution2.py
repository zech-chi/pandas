import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    teacher = teacher.groupby("teacher_id")
    teacher = teacher['subject_id'].nunique().reset_index()
    teacher = teacher.rename({'subject_id': 'cnt'}, axis=1)
    return teacher
