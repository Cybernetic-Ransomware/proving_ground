import pandas as pd
import snscrape.modules.twitter as snstwitter

from tqdm import tqdm


scraper_obj = snstwitter.TwitterSearchScraper('#holoEN')
n_tweets = 50

tweets = []
for i, tweet in tqdm(enumerate(scraper_obj.get_items()), desc='Tweets downloading: ', total=n_tweets):
    data = [tweet.date,
            tweet.id,
            tweet.rawContent,
            tweet.user.username,
            tweet.likeCount,
            tweet.retweetCount]
    tweets.append(data)

    if i == n_tweets:
        break


for tweet in tweets:
    if 'Kronii' in tweet[2]:
        print('')
        print(tweet)
print('')


df_tweets = pd.DataFrame(tweets, columns=['date', 'id', 'content', 'username', 'likeCount', 'retweetCount'])
df_tweets.to_feather('tweets.feather')
df_tweets.to_csv('tweets.csv')
print([x for x in df_tweets['content'] if 'Kronii' in x][0])
