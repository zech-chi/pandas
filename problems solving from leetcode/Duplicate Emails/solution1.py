import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    dic = {}
    for i in range(len(person)):
      if person.email[i] in dic:
        dic[person.email[i]] += 1
      else:
        dic[person.email[i]] = 1
    
    res = pd.DataFrame(columns=["Email"])
    for email in dic:
      if dic[email] > 1:
        res = res._append({"Email": email}, ignore_index = True)
    return res
