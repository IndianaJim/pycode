from psaw import PushshiftAPI
import datetime

api = PushshiftAPI()

start_time = int(datetime.datetime(2021,4,22).timestamp())

submissions = api.search_submissions(after=start_time,
                            subreddit='wallstreetbets',
                            filter=['url','author', 'title', 'subreddit'], 
                            limit=100)

for submission in submissions:
    #print(submission.created_utc)
    #print(submission.title)
    #print(submission.url)
    words = submission.title.split()
    cashtags = list(set(filter(lambda word: word.lower().startswith('$'), words)))

    if len(cashtags) > 0:
        print(cashtags)
