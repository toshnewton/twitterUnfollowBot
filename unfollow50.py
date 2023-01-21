import os
import logging
import time
import tweepy
from time import sleep
from config import *

logging.basicConfig(format='%(levelname)s [%(asctime)s] %(message)s', datefmt='%m/%d/%Y %r', level=logging.INFO)
logger = logging.getLogger()

def initialize_api():
    api = create_api()
    return api

if __name__ == "__main__":
    api = initialize_api()

    me = "XXX"
    numUnfollows = 000

    logger.info("Gathering Friend's IDs")
    ids = api.friends_ids(me)

    logger.info("Reversing ID Array")
    ids.reverse()

    if (len(ids) >= 4000):
        logger.info("Starting Unfollow")
        i=0
        while i<numUnfollows:
            api.destroy_friendship(ids[i])
            logger.info("Sleeping for 30 seconds")
            time.sleep(30)
            i += 1
        logger.info("Completed removing numUnfollows")

    logger.info("Finished")
