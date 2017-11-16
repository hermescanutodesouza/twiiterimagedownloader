import tweepy
import subprocess
from slugify import slugify


def salvaemhd(twittername):

    namescreen = twittername

    file = open("log.txt","w")

    consumer_key = 'i9qNqtBfy4DN8C8qgklTIxWB5'
    consumer_secret = 'UFgfZTkPz26in1vhSUXad31484lSbfJY13qQyLRyoipYhy6avZ'
    access_token = '15145632-bCfDgJeYpd1OX3Upg0lc24Im6d004xK4fGmgpA3YL'
    access_secret = 'ZUfTH2MjKmsrwndwFz5LZQwc7OA3dvt7YEt35YUijLo2s'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    timeline = api.user_timeline(count=200, screen_name = namescreen ,include_rts=False,exclude_replies=True)
    last_id = timeline[-1].id - 1

    while (True):
        more_tweets = api.user_timeline(count=200, screen_name = namescreen ,include_rts=False,exclude_replies=True, max_id=last_id )
        if (len(more_tweets) == 0):
            break
        else:
            last_id = more_tweets[-1].id - 1
            timeline = timeline + more_tweets
            print(namescreen +": ->Carregando pagina do tweet", last_id )

    number = 0
    for tweet in timeline:
       for media in tweet.entities.get("media",[]):
          if media.get("type",None) == "photo":
              number += 1
              file.write( media["media_url"] + '\n')
              print(namescreen +": ->imagem", number, " = ", media["media_url"])

    file.close()

    try:
        subprocess.check_output("aria2c -ilog.txt -j10 --dir=images/"+slugify(namescreen), shell=True)
    except:
        print(namescreen +": ->Erro no download dos arquivos")