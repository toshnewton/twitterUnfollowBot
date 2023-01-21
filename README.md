# twitterUnfollowBot

## Twitter bot using Tweepy that unfollows the oldest 50 friends.

### Setup
1. Replace the placeholder **XXX** with your corresponding tokens in the credentials.py file
2. Replace the placeholder **XXX** with your screen name (capitalization matters) in the unfollow50.py file
3. Replace the placeholder **000** with desired number of unfollows per file run.
4. Upload all files to your python hosting of your choice, I personally use [PythonAnywhere](https://www.pythonanywhere.com/)

### Application
Unfollowing mass users by hand is a time-consuming task. Especially when you want to unfollow 5,000 users. Twitter rate limits also get in the way, the rate limits are 50 follows or unfollows per 15 minutes. You can change the number of users you want to unfollow in the unfollow50.py file, make sure to change the rate limits to make sure to dont go over. My personal use for this bot on my giveaway bot [@shanknails](https://twitter.com/shanknails) to make sure I dont hit the 5,000 friends limit for unverified accounts.
