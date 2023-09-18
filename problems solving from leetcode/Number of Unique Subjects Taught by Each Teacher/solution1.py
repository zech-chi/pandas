import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    dic = {}
    for i in range(len(teacher)):
        if not teacher.teacher_id[i] in dic:
            dic[teacher.teacher_id[i]] = set()
        dic[teacher.teacher_id[i]].add(teacher.subject_id[i])
    
    data_list = [{"teacher_id": key, "cnt": len(value)} for key, value in dic.items()]
    return pd.DataFrame(data_list)
