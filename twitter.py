# pip install twitterscraper
from twitterscraper import query_tweets

if __name__ == '__main__':
    list_of_tweets = query_tweets("covid-19", limit=None)

    #print the retrieved tweets to the screen:
    index = 0
    for tweet in list_of_tweets:
        print(index, tweet.text)
        index += 1

    #Or save the retrieved tweets to file:
    file = open('output.txt','w')
    for tweet in list_of_tweets:
        file.write(tweet.text + '\n')
    file.close()