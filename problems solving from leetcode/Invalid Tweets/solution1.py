import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    arr = []
    for i in range(len(tweets)):
        if len(tweets.content[i]) > 15:
            arr.append(tweets.tweet_id[i])
    return pd.DataFrame({'tweet_id': arr})
