import sys
sys.dont_write_bytecode = True

import tweepy
import TwitterKeys as keys
from googleapiclient.discovery import build
import YTKeys as yt
import json
import time
import datetime

def globals():
    global check
    check = False
    global LatestVideoFile
    LatestVideoFile = open("LatestVideo.txt", "r+")
    for line in LatestVideoFile:
        pass
    last_line = line
    fileText = str(line)
    global videoID
    videoID = fileText

def ytAPI():
    global youtube
    youtube = build("youtube", "v3", developerKey=yt.API_Key)

def twitterAPI():
    global client
    client = tweepy.Client(keys.Bearer_Token, keys.API_Key, keys.API_Secret_Key, keys.Access_Token, keys.Access_Token_Secret)
    auth = tweepy.OAuth1UserHandler(keys.API_Key, keys.API_Secret_Key, keys.Access_Token, keys.Access_Token_Secret)
    return tweepy.API(auth)

def get_video():
    global videoID, check, LatestVideoFile
    request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            maxResults="1",
            playlistId="UURlvF4jIeBWqXJDGNXfPyVw"
        )
    global response
    response = request.execute()
    json_str = json.dumps(response)
    video = json.loads(json_str)
    global id
    id = video["items"][0]["snippet"]["resourceId"]["videoId"]
    id = str(id)
    if id == videoID:
        check = False
    else:
        check = True
        videoID = id
        LatestVideoFile.write("\n" + id)

def tweet(message):
    client.create_tweet(text=message)
    print("Tweeted Successfully")        

    
if __name__ == "__main__":
    globals()
    twitterAPI = twitterAPI()
    ytAPI = ytAPI()
    while 1:
        now = datetime.datetime.now()
        now = str(now)
        print("Checking Chael Sonnen's YT Channel for new videos... " + now)
        get_video()
        if (check):
            print("TWEET")
            tweet("Check out this new video by The Bad Guy!\nhttps://www.youtube.com/watch?v=" + id)
        time.sleep(1800)