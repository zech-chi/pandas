import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets["len_greater_than_15"] = tweets.content.apply(lambda x: len(x) > 15)
    return tweets.loc[tweets.len_greater_than_15, ["tweet_id"]]
