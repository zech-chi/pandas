import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    emails_counter = person.email.value_counts()
    emails_dup = emails_counter[emails_counter > 1].index.to_list()
    res = pd.DataFrame({"Email": emails_dup})
    return res
