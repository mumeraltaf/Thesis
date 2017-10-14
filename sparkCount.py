Tweets = spark.read.json(hdfsPath + "bigTwitter.json")
print Tweets.filter("json.user.screen_name == 'abc'").count()