import praw
import config
import time
import os

# Logs in user to reddit


def login():
    r = praw.Reddit(username=config.username,
                    password=config.password,
                    client_id=config.client_id,
                    client_secret=config.client_secret,
                    user_agent="kabirpamnani's comment responder v0.1")
    return r

# prints


def run(r, comments_list):
    print("Getting the last 100 comments")

    for comment in r.subreddit('test').comments(limit=100):
        if "cat" in comment.body and comment.id not in comments_list and comment.author != r.user.me():
            print("String with \"cat\" found in comment " + comment.id)
            # comment.reply("I love cats more")
            print("Replied to comment " + comment.id)

            comments_list.append(comment.id)

            with open("comments_list.txt", "a") as f:
                f.write(comment.id + "\n")

    # print(comments_list)

    print("Sleeping for 10 seconds")
    time.sleep(10)


def saved_comments():
    if not os.path.isfile("comments_list.txt"):
        comments_list = []
    else:
        with open("comments_list.txt", "r") as f:
            comments_list = f.read()
            comments_list = comments_list.split("\n")

    return comments_list


r = login()
comments_list = saved_comments()
print(comments_list)

# runs infinitely
while True:
    run(r, comments_list)
